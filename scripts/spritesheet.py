import pygame

from scripts import constants

class SpriteSheet():

    def __init__(self, file, scale):
        self.sheet = pygame.image.load(file).convert_alpha()
        self.scale = scale
        if self.scale > 0:
            self.sheet = pygame.transform.scale(self.sheet,
            (self.sheet.get_size()[0] * self.scale, 
            self.sheet.get_size()[1] * self.scale))

    def get_image(self, x, y, width, height):

        image = pygame.Surface((width * self.scale, height * self.scale)).convert()

        image.blit(self.sheet, (0, 0), (x * self.scale, y * self.scale, width * self.scale, height * self.scale))

        image.set_colorkey((0,0,0))

        return image

