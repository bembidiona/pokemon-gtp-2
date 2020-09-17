from PIL import Image, ImageChops, ImageDraw, ImageFont
import os

# folders = ["output_CHONK1", "output_comprimidos1", "output_comprimidos2"]
folders = ["generated-sprites_lovecraft"]

SCALE = 4
SIZE = (56 * SCALE, 56 * SCALE)

font_file = ImageFont.truetype(os.getcwd() + "/pokefont.ttf", 16)

for filder_index, folder in enumerate(folders):
    images = []

    files = os.listdir(os.getcwd() + f"/{folder}/")
    for i, file_name in enumerate(files):

        # poke_name = file_name.split("_")[1].split(".")[0]

        img = Image.open(os.getcwd() + f"/{folder}/{file_name}")
        img = img.resize((56, 56), Image.NEAREST)
        img = Image.alpha_composite(
            Image.new("RGBA", (56, 56), (202, 220, 159, 255)), img)

        # centar imagen
        pixels = img.load()
        width_range = [0, 55]
        height_range = [0, 55]
        for y in range(56):
            for x in range(56):
                colorin = pixels[x, y]
                # print(colorin)
                if colorin != (202, 220, 159, 255):
                    width_range = [max(width_range[0], x),
                                   min(width_range[1], x)]
                    height_range = [max(height_range[0], y),
                                    min(height_range[1], y)]
        off_x = int(
            (56 - (width_range[1] - width_range[0])) / 2) - width_range[0]
        off_y = int(
            (56 - (height_range[1] - height_range[0])) / 2) - height_range[0]
        img = ImageChops.offset(img, off_x, off_y)

        img = img.resize(SIZE, Image.NEAREST)

        d = ImageDraw.Draw(img)
        d.text((2, 2), f"{filder_index}:{i+1}/{len(files)}", font=font_file, fill=(15, 56, 15))

        images.append(img)

    images[0].save(f'{folder}.gif', save_all=True, append_images=images[1:], optimize=False, duration=800, loop=0)
