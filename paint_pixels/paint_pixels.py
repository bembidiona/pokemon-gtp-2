import pygame
import pygame.freetype  # Import the freetype module.
import sys
from PIL import Image
import os
import random
import math

FPS = 60
PALETTE = [(202, 220, 159), (15, 56, 15), (48, 98, 48),
           (139, 172, 15), (155, 188, 15)]

brush_images_paths = os.listdir("brushstroke_original/")




def load_image(name, tint):
    image = pygame.image.load(f"brushstroke_original/{name}")
    image.fill(PALETTE[tint], special_flags=pygame.BLEND_RGB_MULT)
    image = pygame.transform.rotate(image, random.random()*20)
    scale = 28 + int(random.random() * 10)
    image = pygame.transform.scale(image, (scale, scale))
    return image


class TestSprite(pygame.sprite.Sprite):

    def __init__(self, tint):
        super(TestSprite, self).__init__()
        self.images = []
        for image_name in brush_images_paths:
            self.images.append(load_image(image_name, tint))

        # assuming both images are 64x64 pixels

        self.index = random.randrange(len(brush_images_paths))
        self.image = self.images[self.index]
        self.rect = pygame.Rect(50, 50, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        # el sin ya se morfa 20frames
        # self.rect.x += int(math.sin(pygame.time.get_ticks()/100 + self.rect.y/(56*4)) * 2)


def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500), 0, 32)
    FONT_LOG = pygame.freetype.Font("pokefont.ttf", 18)

    pygame_clock = pygame.time.Clock()

    img = Image.open("poke2.png")
    pix = img.load()

    my_group = pygame.sprite.Group()

    SCALE = 9

    for y in range(56):
        for x in range(56):
            r, g, b, a = pix[x, y]

            if r == 15:
                color_current = 1
            elif r == 48:
                color_current = 2
            elif r == 139:
                color_current = 3
            elif r == 155:
                color_current = 4
            else:  # bg
                color_current = 0

            if color_current != 0:
                my_sprite = TestSprite(color_current)
                my_sprite.rect.x = x * SCALE
                my_sprite.rect.y = y * SCALE
                my_group.add(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        screen.fill((155, 188, 15))

        mysurf = pygame.Surface([500, 500], pygame.SRCALPHA, 32)
        mysurf = mysurf.convert_alpha()

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update()
        my_group.draw(mysurf)

        # paint to screen surface and update
        screen.blit(mysurf, (0, 0))

        FONT_LOG.render_to(screen, (10, 30), f"FPS:{int(pygame_clock.get_fps())}", (0, 0, 0))
        pygame.display.flip()

        pygame_clock.tick(FPS)
        # pygame.image.save(mysurf, "screen.png")

        # pygame.quit()
        # sys.exit(0)

if __name__ == '__main__':
    main()
