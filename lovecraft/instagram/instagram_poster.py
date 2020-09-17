from instabot import Bot 
import os
import time
from random import random
# //////////////////////////////////////////
# //////////////////////////////////////////
mypath =  os.getcwd()
PATH_PHOTOS = mypath + "/photos_jpg/"
# //////////////////////////////////////////
# //////////////////////////////////////////
pokemon_images = os.listdir(PATH_PHOTOS)

bot = Bot()
username = "pokemon.kadath.region"
password = ""
bot.login(username = username, password = password)


pokemons_data_file = open("monster_data.txt", "r", encoding="utf-8")
pokemons_names = []
for line in pokemons_data_file:
	pokemons_names.append(line.replace("\n", ""))

# so the last post are the ones starting with 'A'
pokemons_names.reverse()
pokemon_images.reverse()

for i, e in enumerate(pokemons_names):
    name, alias = e.split("|")

    #IMPORTANT: photos must me in .jpg format
    post_photo = PATH_PHOTOS+pokemon_images[i]
    post_caption = f"{name}\n{alias}\n\n#pokemon #lovecraft #neuralnetworks #generativeart #creativecoding #machinelearning #lavendertown #gameboy #pokemonart"

    bot.upload_photo(post_photo, caption =post_caption)

    wait_time = random()*20+10
    print(f"posted {len(pokemon_images)-i} / {name} / {pokemon_images[i]}")
    print(f"wait: {wait_time}")
    print("-------------------------")
    time.sleep(wait_time)