import pygame

import platforms
import constants

class Level():
    """ Super-class for levels, each level is a child class of this """
    def __init__(self):

        # Set up lists for platforms and walls
        self.platform_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        # Set the background image for the level
        self.background = None

class TestLevel(Level):
    def __init__(self):
        Level.__init__(self)

        self.background = pygame.transform.scale(pygame.image.load("assets/bg/bg1.png"),(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

        self.platform_list = [platforms.Platform(400,5,0,475)]
        
        self.wall_list = [platforms.Wall(1600,50,-800,550),
                        platforms.Wall(50,250,800,450),]
