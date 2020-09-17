import os
from PIL import Image #pip install pillow

mypath =  os.getcwd()
PATH_ORIGINALSX2 = mypath + '/elegidines/'
PATH_ORIGINALS = mypath + '/56/'

pokemons_images = os.listdir(PATH_ORIGINALSX2)



for i, poke_name in enumerate(pokemons_images):
    img = Image.open(PATH_ORIGINALSX2 + poke_name)
    img = img.resize((56, 56), Image.NEAREST)
    img = Image.alpha_composite(
            Image.new("RGBA", (56, 56), (202, 220, 159, 255)), img)
    img.save(PATH_ORIGINALS + "batch_4_" + str(i).zfill(3)+".png")