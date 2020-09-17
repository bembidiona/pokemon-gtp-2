import os
from PIL import Image, ImageOps  #pip install pillow

mypath =  os.getcwd()
PATH_ORIGINALS = mypath + '/original/'
PATH_OUTPUT = mypath + '/original_flip/'

pokemons_images = os.listdir(PATH_ORIGINALS)

for poke_img_name in os.listdir(PATH_ORIGINALS):
    img = Image.open(PATH_ORIGINALS + poke_img_name)
    img = ImageOps.flip(img)
    img.save(PATH_OUTPUT + poke_img_name)