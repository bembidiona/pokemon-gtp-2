import os
from PIL import Image #pip install pillow
import re

mypath =  os.getcwd()
pokedex = open(mypath + "/out_comprimido_2.txt", "r")

names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr.Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]


SIZE = (56, 56)
PALETTE = [(202, 220, 159), (15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
XSCALE = 2

# -------------------- une partes
parts = 2
pokemon_para_unir = ""
pokedex_unido = []
for i, line in enumerate(pokedex):
    pokemon_para_unir += line.replace("\n", " ")
    if (i+1)%parts == 0:
        # print(pokemon_para_unir)
        pokedex_unido.append(pokemon_para_unir)
        pokemon_para_unir = ""
# ----------------------------------

for i, pokemon in enumerate(pokedex_unido):

    x = 0
    y = 0
    img = Image.new("RGBA", SIZE)
    pixels = img.load()

    pokemon_name = names[i]

    # data = data.split("end", 1)[0] # remove all generated stuff after the first 'end'
    data = pokemon.split(" ")

    print(f"{pokemon_name} tokens:{len(data)} charlenght:{len(pokemon)}")

    # continue

    number_consecutive_blank_lines = 0
    for token in data:

        if "@" in token:
            pass
        elif "!" in token:
            #do empy line thing
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
                    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "|"]
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

                    x = x+color_length
                    if x >= 56:
                        x = 55
            # new line
            x = 0
            y += 1
            if y >= 56:
                y = 55

    img = img.resize((SIZE[0]*XSCALE, SIZE[1]*XSCALE), Image.NEAREST)
    img.save(mypath + f"/output/{i}_{pokemon_name}.png")