import os
from PIL import Image #pip install pillow

mypath =  os.getcwd()


pokedex = open(mypath + "/pokedex.txt", "r")

pokedex = [
'''ramoncito3 : 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|39 2|2 0|19 - 0|10 1|2 0|5 1|2 0|9 2|1 4|2 3|1 2|1 0|1 2|1 4|2 1|1 0|16 - 0|10 1|3 0|4 1|1 2|2 3|1 1|1 0|5 1|1 2|1 0|4 2|1 3|1 1|1 4|1 2|2 0|16 - 0|10 1|1 4|2 1|1 0|2 1|1 4|1 1|1 3|2 1|1 0|3 2|1 1|3 0|5 1|1 4|1 2|2 4|1 1|1 3|1 1|1 0|15 - 0|10 1|1 4|3 1|1 0|2 1|1 4|1 1|1 3|1 4|1 1|1 3|1 1|2 0|5 1|1 2|3 4|1 2|3 4|3 1|1 0|14 - 0|10 1|1 4|4 2|1 4|1 2|1 1|1 4|5 2|1 1|1 4|1 2|1 1|3 2|2 1|1 2|4 4|1 3|1 4|2 1|1 0|13 - 0|10 1|1 4|1 1|2 4|1 1|7 4|3 3|1 1|2 4|1 1|2 4|3 1|1 2|2 3|2 4|3 2|1 0|12 - 0|11 1|1 4|1 1|1 4|1 1|1 2|19 1|1 4|1 1|3 2|1 1|1 4|2 2|3 0|2 2|1 4|1 2|1 4|1 1|1 0|12 - 0|12 1|10 4|4 3|1 2|2 1|1 4|2 2|1 1|1 4|5 1|1 0|4 1|1 0|12 - 0|13 1|1 2|1 4|1 1|1 2|2 1|1 2|3 1|1 4|2 3|1 2|6 0|5 1|1 4|4 1|1 0|13 - 0|14 1|1 4|1 2|1 1|1 2|3 1|1 3|2 1|1 3|2 2|7 0|5 1|1 4|3 1|1 0|13 - 0|15 1|1 3|1 2|2 1|2 2|1 1|1 3|2 1|1 2|7 1| 2|1 0|1 1|1 4|3 3|1 4|2 1|1 0|13 - 0|3 1|4 2|2 1|2 2|2 3|2 2|4 1|1 2|2 1|1 3|1 1| 2|10 1|1 3|4 2|1 4|2 1|1 0|12 - 0|3 1|1 3|4 2|2 1|1 3|3 2|2 1|1 2|14 1|1 3|1 1|1 3|1 1|1 4|3 3|1 2|1 1|1 2|1 0|13 - 0|3 1|1 3|3 1|2 2|3 1|3 2|2 1|2 2|3 1|2 2|6 1|1 3|2 1|1 3|1 2|2 1|1 2|2 1|1 0|16 - 0|4 1|5 3|1 1|2 2|5 1|1 2|2 1|4 2| 2|3 1|1 2|2 3|1 1|1 4|1 3|1 1|2 2|2 1|1 0|17 - 0|8 1|4 2|7 1|2 2|8 1|1 2|4 1|4 0|18 - 0|10 1|1 2|2 1|4 2|3 1|7 2|3 1|1 2|3 3|1 4|1 3|1 1|1 0|19 - 0|11 1|1 2|1 1|3 2|2 1|2 0|1 1|2 2|2 1|2 2|4 3|1 4|4 3|1 2 - 0|56 0|56 0|56 0|56 end'''
]

print(len(pokedex[0]))

SIZE = (56, 56)
PALETTE = [(202, 220, 159), (15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
XSCALE = 3
for i, pokemon in enumerate(pokedex):

    x = 0
    y = 0
    img = Image.new("RGBA", SIZE)
    pixels = img.load()

    pokemon_name, data = pokemon.split(":") 
    pokemon_name = pokemon_name[0:-1] #remove last blank space
    data = data.split("-")

    for line in data:
        tokens = line.split(" ")

        # paint a line
        for token in tokens:            
            if token not in ["", "\n", "end"]:

                try:
                    color_index = int(token.split("|")[0])
                    color_duration = int(token.split("|")[1])
                except:
                    print("Nothing went wrong") 
                else:

                    if color_duration >= 56:
                        color_duration = 55                

                    for x_virtual in range(color_duration):
                        
                        _x = x + x_virtual

                        if _x >= 56:
                            _x = 55
                        # print(f"{_x}:{y}")
                        pixels[_x, y] = PALETTE[color_index]

                    x = x+color_duration
                    if x >= 56:
                        x = 55

        # new line
        x = 0
        y += 1
        if y >= 56:
            y = 55

    img = img.resize((SIZE[0]*XSCALE, SIZE[1]*XSCALE), Image.NEAREST)
    img.save(mypath + f"/output/{i}_{pokemon_name}.png")








