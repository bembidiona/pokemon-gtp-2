from PIL import Image, ImageOps, ImageChops, ImageDraw, ImageFont
import os

# folders = ["output_CHONK1", "output_comprimidos1", "output_comprimidos2"]
folders = ["clean"]

PATH_OUTPUT = os.getcwd() + "/output/"

SIZE = (56, 56)

monster_data = open("monster_data.txt", "r", encoding="utf-8").read().split("\n")

FONT = ImageFont.truetype(os.getcwd() + "/pokefont.ttf", 8)
print(FONT.getmetrics())

BACKGROUND_COLOR = (202, 220, 159, 255)

for filder_index, folder in enumerate(folders):
    images = []

    files = os.listdir(os.getcwd() + f"/{folder}/")
    for i, file_name in enumerate(files):

        # poke_name = file_name.split("_")[1].split(".")[0]

        img = Image.open(os.getcwd() + f"/{folder}/{file_name}")
        img = img.resize((56, 56), Image.NEAREST)
        # img = Image.alpha_composite(Image.new("RGBA", (56, 56), BACKGROUND_COLOR), img)

        # centrar imagen
        pixels = img.load()
        width_range = [0, 55]
        height_range = [0, 55]
        for y in range(56):
            for x in range(56):
                colorin = pixels[x, y]
                # print(colorin)
                if colorin == BACKGROUND_COLOR:
                    pixels[x, y] = (0, 0, 0, 0)
                else:
                    width_range = [max(width_range[0], x),
                                   min(width_range[1], x)]
                    height_range = [max(height_range[0], y),
                                    min(height_range[1], y)]
        off_x = int((56 - (width_range[1] - width_range[0])) / 2) - width_range[0]
        off_y = int((56 - (height_range[1] - height_range[0])) / 2) - height_range[0]
        img = ImageChops.offset(img, off_x, off_y)

        img = img.resize(SIZE, Image.NEAREST)

        img = ImageOps.expand(img, SIZE[0]*3, fill=(0, 0, 0, 0))

        d = ImageDraw.Draw(img)

        monster_name, monster_description = monster_data[i].split("|")

        monster_name_size = FONT.getsize(monster_name, direction=None, features=None, language=None, stroke_width=0)
        monster_description_size = FONT.getsize(monster_description, direction=None, features=None, language=None, stroke_width=0)
        
        _y = 80        
        d.text((int(img.size[0]/2 - monster_name_size[0]/2), _y), monster_name, font=FONT, fill=(15, 56, 15))
        d.text((int(img.size[0]/2 - monster_description_size[0]/2), _y+14), monster_description, font=FONT, fill=(15, 56, 15))

        img.save(f"{PATH_OUTPUT}lovemones_{str(i).zfill(3)}.png")
