import os
from PIL import Image #pip install pillow

mypath =  os.getcwd()


pokedex = open(mypath + "/pokedex.txt", "r")

SIZE = (56, 56)
PALETTE = [(202, 220, 159), (15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
XSCALE = 2
for i, pokemon in enumerate(pokedex):

    x = 0
    y = 0
    img = Image.new("RGBA", SIZE)
    pixels = img.load()

    pokemon_name, data = pokemon.split(":", 1)
    pokemon_name = pokemon_name[0:-1] #remove last blank space

    # data = data.split("end", 1)[0] # remove all generated stuff after the first 'end'
    data = data.split(" ")

    print(f"{pokemon_name} lines:{len(data)} lenght:{len(pokemon)}")

    number_consecutive_blank_lines = 0
    for line in data:

        line_data = line.split("|")
        # paint a line
        for unidad in line_data:

            if unidad not in ["", "\n", "end", ':']:

                try:
                    # unidad = unidad.replace("]", "")
                    color_index = int(unidad.split("-")[0])
                    color_duration = int(unidad.split("-")[1])
                except:
                    print(f"WEIRD CHORIZO: {unidad}") 
                else:
                     

                    if color_duration > 56:
                        color_duration = 56
                    elif color_duration == 56: # if there are too many blank lines, just skip it
                        number_consecutive_blank_lines += 1
                        if number_consecutive_blank_lines > 16:
                            y -= 1
                            continue
                    else:
                        number_consecutive_blank_lines = 0

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








