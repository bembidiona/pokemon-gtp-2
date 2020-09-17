import os
from PIL import Image #pip install pillow

mypath =  os.getcwd()
im = Image.open(mypath + '/pokedex.png')

pix = im.load()
size = (56, 56)
gfxbitty = ""


# hola = '''
# Bulbasaur 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|35 1|1 0|20 - 0|34 1|1 4|1 2|1 0|19 - 0|33 1|1 4|2 1|1 2|1 0|18 - 0|29 2|1 1|3 4|2 2|1 3|1 1|1 0|18 - 0|26 2|1 1|2 4|1 1|1 3|1 4|3 1|1 3|1 1|1 0|18 - 0|23 2|1 1|2 4|3 1|1 3|1 4|2 3|1 2|1 1|1 3|1 1|1 0|18 - 0|22 1|1 4|3 2|1 1|1 3|1 4|3 3|2 1|1 2|1 3|1 1|1 0|18 - 0|21 1|1 4|2 1|1 3|1 4|4 3|3 2|1 1|1 2|1 3|1 2|1 1|1 0|17 - 0|20 1|1 2|1 3|1 1|1 3|1 4|3 3|3 2|3 1|1 3|1 4|1 3|1 1|2 0|16 - 0|19 1|1 2|2 1|1 2|2 4|1 1|3 2|4 1|1 2|1 3|1 4|1 3|1 1|1 2|1 1|1 0|15 - 0|14 1|3 0|2 1|1 2|2 1|1 2|2 1|1 4|2 3|1 1|1 2|3 1|1 2|1 3|1 4|1 3|1 2|1 1|1 2|1 1|1 0|14 - 0|13 1|1 4|1 3|2 1|1 0|1 1|6 4|2 3|2 2|1 1|1 2|2 1|1 2|1 3|1 4|1 3|2 1|1 2|1 1|1 0|14 - 0|13 1|1 4|2 3|1 1|2 3|5 1|1 3|3 2|2 1|1 2|1 1|1 2|1 3|1 4|2 3|2 2|1 1|1 3|1 1|1 0|13 - 0|13 1|1 4|6 3|5 1|1 3|1 2|2 1|1 2|1 1|1 2|2 3|1 4|2 3|1 2|2 1|1 3|1 1|1 0|13 - 0|14 1|1 4|5 3|1 1|2 3|2 2|5 1|2 2|1 3|1 4|2 3|2 2|2 1|1 3|1 1|1 0|13 - 0|13 1|1 4|5 3|1 1|2 3|2 2|1 1|1 2|5 1|2 2|1 3|3 2|3 1|1 4|1 1|1 0|13 - 0|12 1|1 4|2 1|1 4|2 3|5 2|1 1|2 2|3 1|1 2|2 1|2 2|5 1|1 2|1 4|1 1|1 0|13 - 0|12 1|1 4|1 1|1 4|1 1|1 3|5 2|1 1|1 4|1 3|1 1|1 2|2 1|2 2|3 1|1 2|3 1|1 2|1 4|1 3|1 1|1 0|13 - 0|12 1|2 3|1 1|2 3|5 2|1 1|2 3|2 1|1 2|7 1|3 2|1 4|1 3|1 2|2 0|13 - 0|11 1|1 4|1 1|1 4|1 1|1 3|7 1|2 4|2 1|1 2|5 1|1 2|2 1|1 2|1 3|2 2|1 1|1 0|14 - 0|11 1|1 3|12 2|1 1|3 2|4 1|2 2|2 1|1 2|3 1|1 0|15 - 0|10 1|1 4|1 2|1 1|1 2|1 1|8 2|1 1|1 4|3 1|1 2|3 1|2 2|2 1|4 0|16 - 0|10 4|1 1|1 4|1 3|1 1|10 4|4 3|1 1|1 2|7 1|2 0|17 - 0|9 1|2 4|4 3|1 2|1 3|6 1|1 4|4 3|2 2|1 1|1 2|2 1|2 2|2 1|1 0|17 - 0|10 1|1 4|5 1|8 4|3 3|3 2|9 1|1 0|16 - 0|11 1|1 4|3 3|2 1|1 4|6 1|1 4|1 3|3 2|4 1|1 3|2 2|4 1|1 0|15 - 0|12 1|1 2|1 3|2 2|2 1|1 4|4 3|2 2|1 1|1 3|1 2|2 1|1 2|1 1|1 2|1 4|1 3|3 2|2 1|1 0|15 - 0|14 2|1 1|3 2|1 1|1 3|7 1|3 2|2 1|1 3|1 4|2 3|3 2|1 1|2 0|14 - 0|18 1|1 4|1 2|1 1|1 3|4 2|5 1|1 2|1 4|4 3|2 2|2 1|1 0|14 - 0|18 1|1 4|2 3|1 2|1 1|2 2|6 1|1 3|1 4|4 3|2 2|2 1|1 0|14 - 0|18 2|1 4|3 3|2 2|1 1|7 2|1 3|1 4|3 3|2 2|2 1|1 0|14 - 0|19 1|1 4|2 3|3 2|4 1|1 0|1 1|2 2|1 3|1 4|1 3|2 2|3 1|1 0|14 - 0|20 2|1 1|1 3|2 2|4 1|1 2|1 1|1 0|1 1|2 2|6 1|1 0|15 - 0|22 2|1 1|4 2|3 1|1 0|3 1|3 2|3 1|1 0|15 - 0|26 1|1 2|2 1|1 0|5 1|1 2|3 1|1 0|16 - 0|27 1|2 0|7 1|3 0|17 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 - 0|56 end
# '''
# print(len(hola.split(" ")))

names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr.Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]



output_txt = ""
SPACE = " "
LINEBREAK = "-"

for poke_number in range(0, 151):

    color_past = None
    color_continuo = 1
    
    output_txt += f"{names[poke_number]} : "
    # output_txt += "start "
    gfxbitty = ""
    # print("Processing: #"+ str(poke_number + 1).zfill(3) +" "+names[poke_number])

    poke_x = poke_number % 10 * size[0]
    poke_y = int(poke_number / 10) * size[1]

    for y in range(poke_y, poke_y + size[1]):
        for x in range(poke_x, poke_x + size[0]):

            r,g,b,a = pix[x,y]

            if a == 0:
                color_current = 0
            elif r == 0:
                color_current = 1
            elif r == 105:
                color_current = 2
            elif r == 197:
                color_current = 3
            elif r == 255:
                color_current = 4

            if x == poke_x:
                color_past = color_current
                color_continuo = 1
            else:            
                if color_current == color_past:
                    color_continuo += 1
                else:
                    gfxbitty += f"{color_past}|{color_continuo}" + SPACE

                    color_past = color_current
                    color_continuo = 1 

        gfxbitty += f"{color_past}|{color_continuo}" + SPACE
        gfxbitty += LINEBREAK + SPACE

    gfxbitty = gfxbitty[0:-2] + "end"
    output_txt += gfxbitty + " \n"
    
text_file = open(mypath + "/pokedex.txt", "w")
text_file.write(output_txt)
text_file.close()





