// ---------------------------
// START SERVER AND PROXYSPACE
// ---------------------------
(
//increase number of buffers the server has access to for loading samples
s.options.numBuffers = 1024 * 16;
//increase the memory available to the server
s.options.memSize = 8192 * 64;
//boot the server
s.boot;

//start proxyspace
p=ProxySpace.push(s);
//start tempo clock
p.makeTempoClock;
//give proxyspace a tempo
p.clock.tempo = 2;

//display guis
ProxyMixer(p);
s.meter;
s.scope;

//activate StageLimiter (needs BatLib Quark)
StageLimiter.activate;
"-- DONE! --".postln;
)

// ---------------------------
// ADD SYNTHS
// ---------------------------
(
SynthDef(\wave, {|out, sustain=0, amp=1, freq=440, pan=0, env = #[0, 1, 0, 1], wobbly=0, chip=0, vib = #[0, 0]|
    var sig;
    var envelope = EnvGen.ar(Env.linen(env[0], env[1], env[2], 1, \lin), timeScale:sustain*env[3], doneAction:2);
    var wobblyenv = LFPulse.kr(10, 0.5, mul:wobbly).range(2, 1);
    var chipenv = if(chip>0, EnvGen.kr(Env.new([2, 2, 1, 1], [0.05, 0, 0.1], 0, 4, 4)), 1);

    // freq stuff
    freq = freq	* wobblyenv	* chipenv + SinOsc.kr(vib[0]).range(0, vib[1]);

    sig = Decimator.ar(LFTri.ar(freq), 441000, 8);
    sig = sig*amp*0.2;
    OffsetOut.ar(out, Pan2.ar(sig*0.8, pan, envelope));
}).add;

SynthDef(\pulse, {|out, sustain=0, freq=440, pan=0, amp=1, env = #[0, 1, 0, 1],
    width=0.5, wobbly=0, chip=1, vib = #[0, 0]|

    var sig;
    var envelope = EnvGen.ar(Env.linen(env[0], env[1], env[2], 1, \lin), timeScale:sustain*env[3], doneAction:2);
    var pulse_width = Select.kr((width%3).floor, [0.125, 0.25, 0.5]);
    var wobblyenv = LFPulse.kr(10, 0.5, mul:wobbly).range(2, 1);
    var chipenv = if(chip>0, EnvGen.kr(Env.new([2, 2, 1, 1], [0.05, 0, 0.1], 0, 4, 4)), 1);

    // freq stuff
    freq = freq	* wobblyenv	* chipenv + SinOsc.kr(vib[0]).range(0, vib[1]);

    //generate channel
    sig = Pulse.ar(freq, pulse_width);
    sig = sig*amp*0.1;
    OffsetOut.ar(out, Pan2.ar(sig, pan, envelope));
}).add;

SynthDef(\noise, {|out, sustain=0, amp = 1, freq=440,pan=0, env = #[0, 1, 0, 1]|
    var sig;
    var envelope = EnvGen.ar(Env.linen(env[0], env[1], env[2], 1, \lin), timeScale:sustain*env[3], doneAction:2);
    var noise_freq = Select.kr((freq%13).floor, [1.0,2.0,4.0,5.34,8.0,10.68,16.0,19.03,25.4,32.0,42.71,64.0,128.0]);

    sig = Decimator.ar(Latch.ar(LPF.ar(WhiteNoise.ar,3000), Impulse.ar(220*noise_freq),44100,4));
    sig = sig*amp*0.2;
    OffsetOut.ar(out, Pan2.ar(sig*0.8, pan, envelope));
}).add;


(
SynthDef(\ps, { |out = 0, bufnum, envBufnum, pan = 0, stretch = 5, window = 0.25, amp = 1|
	var trigPeriod, sig, chain, trig, pos, fftSize;

    // Calculating fft buffer size according to suggested window size
    fftSize = 2**floor(log2(window*SampleRate.ir));
    // Grain parameters
    // The grain is the exact length of the FFT window
    trigPeriod = fftSize/SampleRate.ir;
    trig = Impulse.ar(1/trigPeriod);
    pos = Demand.ar(trig, 0, demandUGens: Dseries(0, trigPeriod/stretch));
    // Extraction of 2 consecutive grains
    // Both grains need to be treated together for superposition afterwards
    sig = [GrainBuf.ar(1, trig, trigPeriod, bufnum, 1, pos, envbufnum: envBufnum),
        GrainBuf.ar(1, trig, trigPeriod, bufnum, 1, pos + (trigPeriod/(2*stretch)), envbufnum: envBufnum)]*amp;
    // FFT magic
    sig = sig.collect({ |item, i|
        chain = FFT(LocalBuf(fftSize), item, hop: 1.0, wintype: -1);
        // PV_Diffuser is only active if its trigger is 1
        // And it needs to be reset for each grain to get the smooth envelope
        chain = PV_Diffuser(chain, 1 - trig);
        item = IFFT(chain, wintype: -1);
    });
    // Reapply the grain envelope because the FFT phase randomization removes it
    sig = sig*PlayBuf.ar(1, envBufnum, 1/(trigPeriod), loop:1);
    // Delay second grain by half a grain length for superposition
    sig[1] = DelayC.ar(sig[1], trigPeriod/2, trigPeriod/2);
    // Panned output
    Out.ar(out, Pan2.ar(Mix.new(sig), pan));
}).add;
)
);


// ---------------------------
// LIVECODED STUFF
// ---------------------------

p.clear

~p1.fadeTime = 0;
~out.stop(4)

(
p.clock.tempo = 0.25;
p.quant = 1;
n = [-24, 0, 7];
// n = [0];
~blip = Pbind(\instrument, \pulse,
	\note, Pseq([0, 7, 11, 6], inf) + 12 + n,
    \dur, 1,
	\chip, 1,
	\wobble, 0.2,
	\env, Pseq([[[0, 1, 0.1, 0.1]], [[0.1, 0, 0.9, 0.2]]], inf),
    \pan, Pseq([-1, 1], inf),
	\amp, 0.7,
);


~p1 = Pbind(\instrument, \pulse,
	\note, Pseq([0, 7, 11, 6], inf) + 12 + n,
    \dur, 1,
    \env, [[0.6, 0.1, 1.7, 3.1]],
    \pan, Pseq([-1, 1], inf),
	\amp, Pseq([1, 0.5, 1, 0.7], inf) * 0.1,
);
~p2 = Pbind(\instrument, \pulse,
    \note, Pseq([7, 7, 4, 4,  7,6,4,11, 1, 1,   7, 7, 6, 6, 11,7,6,11, 12, 12], inf) + [0] + n,
    \dur, Pseq([2, 2, 2, 2, 1, 1, 1, 1, 2, 2], inf),
    // \dur, 0.025,
    \vib, [[10, 6]],
    \wobbly, 0.001,
    \width, Pseq((0..10), inf),
    \amp, 0.2,
    \env, [[0.6, 0.7, 0.6, 3]],
    \chip, 1,
);
~p3 = Pbind(\instrument, \pulse,
    \note, Pseq([0, 7, 11, 6], inf) +(12*2) + n,
    \amp, 0.05,
    \chip, 1,
    \env, [[0.2, 1, 0.2, 0.8]],
    \dur, 0.025,
    \pan, Pwhite()*0.25,
);
~wave = Pbind(\instrument, \wave,
	\note, Pseq([4, 2, 0, 4,0,-1,4], inf) + [-12, -24]+ n,
    \dur, Pseq([4, 4, 4, 1, 1, 1, 1], inf),
    \vib, [[0.5, 3]],
    \wobbly, 0.05,
    \amp, 0.2,
    \env, [[0.3, 0.7, 0.3, 4]],
);

~noise = Pbind(\instrument, \noise,
    \note, Pseq([1, \, \, \], inf), //13 values
    \dur, 1,
    \env, [[0.8, 0.2, 0.8, 2]],
    \amp, 0.3,
    \pan, 0
);

// [a, b, c].sum
~mix = {RLPF.ar([~blip*0.06, ~p1*0, ~p2*0, ~p3*0.6, ~wave*0, ~noise*0.2].sum * 0.4, SinOsc.kr(0.025).range(2000, 4000))};
~out = {FreeVerb.ar(~mix, 1, 9, 2)*2+ ~mix+ (~cry*MouseX.kr*0.3)};
// ~out = ~noise;
~out.play;
)
~out.stop(4)

thisProcess.platform.recordingsDir

p.clear

p.fadeTime=4;

~cry.clear;
~cry.stop;

~cry.clear

(
var envBuf, envSignal, buffer;
buffer = Buffer.read(s, "C:/JERE/PROJECTS/organelle/PokeHex/cries/25.wav");
// The grain envelope
envBuf = Buffer.alloc(s, s.sampleRate, 1);
envSignal = Signal.newClear(s.sampleRate).waveFill({|x| (1 - x.pow(2)).pow(1.25)}, -1.0, 1.0);
envBuf.loadCollection(envSignal);
// Runs indefinitely
~cry = Pmono(\ps, \stretch, 50, \amp, 0.2, \bufnum, buffer.bufnum, \envBufnum, envBuf.bufnum);
)

ProxyMixer(p);


