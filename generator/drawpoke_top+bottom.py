import os
from PIL import Image  # pip install pillow
import re

mypath = os.getcwd()
pokedex_top = open(mypath + "/output_top.txt", "r").read().split("\n")
pokedex_bottom = open(mypath + "/output_bottom.txt", "r").read().split("\n")

names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel",
         "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr.Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
names = ['Abholos', 'Alala', 'Ammutseba', 'Amon-Gorloth', 'Aphoom-Zhah', 'Apocolothoth', 'Arwassa', 'Atlach-Nacha', "Ayi'ig", 'Aylith', "Baoht Z'uqqa-Mogg", 'Basatan', "B'gnu-Thun", 'Bokrug', 'Bugg-Shash', 'Byagoona', 'Byatis', 'Chaugnar Faugn', 'Coatlicue', 'The Color', 'Coinchenn', 'Crom Cruach', 'Cthaat', 'Cthaeghya', 'Cthugha', 'Cthulhu', 'Cthylla', 'Ctoggha', 'Cyäegha', 'Cynothoglys', 'Dhumin', 'Dygra', 'Dythalla', 'Dzéwà', 'Eihort', "Ei'lor", 'Etepsed Egnis', 'Ghadamon', 'Ghatanothoa', 'Ghisguth', 'Gi-Hoveg', "Gla'aki", 'Gleeth', 'Gloon', 'Gobogeg', 'God of the Red Flux', 'Gog-Hoor', 'Gol-goroth', 'Golothess', 'The Green God', 'Groth-Golka', 'Gtuhanai', 'Gurathnaka', "Gur'la-ya", 'Gwarloth', 'Gzxtyos', 'Han', 'Hastalÿk', 'Hastur', "H'chtelegoth", 'Haiogh-Yai', 'Hnarqu', 'Hziulquoigmnzhah', 'Idh-yaa', 'Inpesca', 'Iod', 'Istasha', 'Ithaqua', "Janai'ngo", 'Juk-Shabb', 'Kaalut', "Kag'Naru of the Air", 'Kassogtha', 'Kaunuzoth', "Khal'kru", 'Klosmiebhyx', "K'nar'st", 'Krang', "Kthaw'keth", 'Kurpannga', 'Lam', "Lexur'iga-serr'roth", 'Lythalia', 'Mappo no Ryujin', "M'basui Gwandu", "M'Nagalah", 'Mnomquah', 'Mordiggian', 'Mormo', 'Mortllgh', 'Mynoghra', 'Nctosa & Nctolhu', "Ngirrth'lu", 'Northot', 'Nssu-Ghahnb', 'Nug and Yeb', 'Nyaghoggua', 'Nycrama', 'Nyogtha', "Ob'mbu", 'Oorn', 'Othuum', 'Othuyeg', 'Perse', 'Pharol', 'Poseidon', 'Psuchawrl', 'Ptar-Axtlan', 'Quachil Uttaus', 'Quyagen', "Q'yth-az", "Raandaii-B'nk", 'Ragnalla', 'Raphanasuan', 'Rhagorthua', 'Rhan-Tegoth', 'Rhogog', "Rh'Thulla of the Wind", 'Rlim Shaikorth', 'Rokon', 'Saaitii', 'Scathach', 'Sebek', 'Sedmelluq', 'Sfatlicllp', 'Shaklatal', 'Shathak', 'Shaurash-Ho', 'Sheb-Teth', 'Shista', 'Shlithneth', 'Sho-Gath', 'Shterot', "Shudde M'ell", 'Shuy-Nihl', 'Sthanee', "S'tya-Yg'Nalle", 'Summanus', 'Swarog', 'Thanaroa', 'Tharapithia', 'Thasaidon', "T'ith", 'Thog', 'Toth', "Th'rygh", 'Tsathoggua', 'Tulushuggua', 'Turua', 'Uitzilcapac', "Ut'Ulls-Hr'Her", 'Vhuzompha', 'Vibur', 'Vile-Oct', 'Volgna-Gath', 'Voltiyig', 'Vthyarilops', 'Vulthoom', 'The Worm that Gnaws in the Night', 'Xalafu', 'Xcthol', 'Xinlurgash', 'Xirdneth', 'Xitalu', 'Xotli', 'Xoxiigghua', 'Yamath', 'Yegg-Ha', "Y'golonac", 'Yhagni', 'Yhashtur', 'Yig', "Y'lla", "'Ymnar", 'Yog-Sapha', 'Yorith', 'Ysbaddaden', 'Ythogtha', 'Yug-Siturath', 'Zathog', 'Zhar and Lloigor', 'Zindarak', 'Zoth-Ommog', 'Zstylzhemghi', 'Zushakon', "Z'toggua", 'Zvilpogghua']

SIZE = (56, 56)
PALETTE = [(202, 220, 159), (15, 56, 15), (48, 98, 48),
           (139, 172, 15), (155, 188, 15)]
XSCALE = 4


def remove_extra_lines(part, flip=False, remove_extra_emptys=True):
    listita = part.split(" ")

    # check for empty lines
    empty_lines_len = 0
    for token_index, temp_token in enumerate(listita):
        if "!" in temp_token:
            for char_index, char in enumerate(temp_token):
                if char == "!":
                    try:
                        empty_lines_len = int(temp_token[char_index + 1])
                    except:
                        print(f"WEIRD !lines in bottom: {names[i]} // token: {temp_token}")
                    else:
                        listita[token_index] = f"!{empty_lines_len}"
                    break
            break

    # this expect to remove all !tokens after the first aparition
    if remove_extra_emptys:
    	curated_list = []
    	free_pass = True
    	for item in listita:
    		if "!" in item:
    			if free_pass:
    				curated_list.append(item)
    				free_pass = False
    		else:
    			curated_list.append(item)
    	listita = curated_list

    # reverse
    if flip:
        listita.reverse()
    # remove extra lines. max of lines for bottom is 28
    bottom_exceso = (len(listita) - 1 + empty_lines_len) - 28
    if bottom_exceso > 0:
        listita = listita[0:-bottom_exceso]

    # join list ot a silen txt line and return
    return " ".join(listita)

# -------------------- une partes
pokemon_para_unir = ""
pokedex_unido = []
for i, name in enumerate(names):
    pokemon_para_unir += f"{name}: "

    part_top = pokedex_top[i]
    part_top = part_top.replace("\n", " ")
    part_top = part_top.split(":")[1]
    # check for empty lines
    part_top = remove_extra_lines(part_top, flip=False)
    # add
    pokemon_para_unir += part_top

    pokemon_para_unir += " -2- "
    # --- part bottom
    part_bottom = pokedex_bottom[i]
    part_bottom = part_bottom.replace("\n", " ")
    part_bottom = part_bottom.replace("END", "")  # discart END tag on bottoms
    part_bottom = part_bottom.split(":")[1]  # discart name tag
    # check for empty lines
    part_bottom = remove_extra_lines(part_bottom, flip=True)
    # add
    pokemon_para_unir += part_bottom

    # add poke to main list
    pokedex_unido.append(pokemon_para_unir)
    pokemon_para_unir = ""
# ----------------------------------

for i, pokemon in enumerate(pokedex_unido):

    x = 0
    y = 0
    img = Image.new("RGBA", SIZE)
    pixels = img.load()

    pokemon_name = names[i]

    # data = data.split("end", 1)[0] # remove all generated stuff after the
    # first 'end'
    data = pokemon.split(" ")

    # print(f"{pokemon_name} tokens:{len(data)} charlenght:{len(pokemon)}")

    number_consecutive_blank_lines = 0
    for token in data:

        if "@" in token:
            pass
        elif "-2-" in token: # estarting bottom part
            pass
        elif "!" in token:
            # do empy line thing
            try:
                number_of_empty_lines = int(token.split("!")[1])
                for empty_line in range(number_of_empty_lines):
                    for _x in range(SIZE[0]):
                        pixels[_x, y] = PALETTE[0]
                    y += 1
            except:
                continue
        elif "END" in token:
            pass
        else:
            # print(token)
            token_units = re.findall(r"[0-9][a-zA-Z|]", token)
            # print(token_units)
            for unidad in token_units:
                try:
                    # unidad = unidad.replace("]", "")
                    color_index = int(unidad[0])
                    color_length = unidad[1]
                    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                           "z", "A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "|"]
                    color_length = abc.index(color_length)
                except:
                    print(f"WEIRD UNIT: {unidad}")
                else:
                    for x_virtual in range(color_length):

                        _x = x + x_virtual

                        if _x >= 56:
                            _x = 55
                        if y >= 56:
                            y = 55
                        # print(f"{_x}:{y}")
                        color_index = max(min(color_index, 4), 0)
                        pixels[_x, y] = PALETTE[color_index]

                    x = x + color_length
                    if x >= 56:
                        x = 55
            # new line
            x = 0
            y += 1
            if y >= 56:
                y = 55

    img = img.resize((SIZE[0] * XSCALE, SIZE[1] * XSCALE), Image.NEAREST)
    img.save(mypath + f"/generated-sprites/{str(i).zfill(3)}_{pokemon_name}.png")
