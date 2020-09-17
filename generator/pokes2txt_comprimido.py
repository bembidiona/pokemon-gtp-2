import os
from PIL import Image #pip install pillow

mypath = os.getcwd()
size = (56, 56)

# names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr.Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

output_txt = ""
poke_data = ""
color_index = 0
color_length = 0
lineas_vacias_continuas = 0

def add_pixels(color_index, color_length):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    code = "|"
    try:
        code = abc[color_length]
    except:
        print(f"SPIL len of color: {color_length}")

    return f"{color_index}{code}"

def add_to_data():
    global poke_data
    global color_index
    global color_length
    global lineas_vacias_continuas

    if color_length == 56:
        lineas_vacias_continuas += 1
    elif lineas_vacias_continuas == 0:
        poke_data += add_pixels(color_index,color_length)
    else:
        poke_data += f"!{lineas_vacias_continuas} "
        poke_data += add_pixels(color_index,color_length)
        lineas_vacias_continuas = 0


pokemon_sprites = os.listdir(mypath + "/original")
for poke_number, poke_filename in enumerate(pokemon_sprites):

    im = Image.open(mypath + '/original/' + poke_filename)
    pix = im.load()

    color_index = None
    color_length = 1
    
    output_txt += f"{poke_number}@1 "
    poke_data = ""

    lineas_vacias_continuas = 0

    for y in range(size[1]):
        # poke_data += "["

        if y == 28:
            poke_data += f"{poke_number}@2 "

        for x in range(size[0]):

            r,g,b,a = pix[x,y]

            if r == 15:
                color_current = "1"
            elif r == 48:
                color_current = "2"
            elif r == 139:
                color_current = "3"
            elif r == 155:
                color_current = "4"
            else: # bg
                color_current = "0"

            if x == 0:
                color_index = color_current
                color_length = 1
            else:            
                if color_current == color_index:
                    color_length += 1
                else:

                    add_to_data()

                    color_index = color_current
                    color_length = 1

        add_to_data()
        poke_data += " "

    # end of poke
    poke_data += f"!{lineas_vacias_continuas} END"
    poke_data = ' '.join(poke_data.split()) # remove extra whitespaces

    # print(len(poke_data))
    output_txt += poke_data

    if poke_number != 150:
        output_txt += " \n"
    
text_file = open(mypath + "/pokedex.txt", "w")
text_file.write(output_txt)
text_file.close()





