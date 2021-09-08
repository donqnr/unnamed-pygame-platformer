import pygame

import platforms
import constants
import enemies

class Level():
    """ Super-class for levels, each level is a child class of this """
    def __init__(self):

        # Set up lists for platforms and walls
        self.platform_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        # Set the background image for the level
        self.background = None

class TestLevel(Level):
    def __init__(self):
        Level.__init__(self)

        self.background = pygame.transform.scale(pygame.image.load("assets/bg/bg1.png"),(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

        self.platform_list = [#platforms.Platform(100,1,0,120),
                            platforms.Gray_Tile_01(48,128),
                            platforms.Gray_Tile_01(56,128),
                            platforms.Gray_Tile_01(64,128),
                            platforms.Gray_Tile_01(72,128),]
        
        self.wall_list = [platforms.Wall(400,10,-200,176),
                        platforms.Wall(12,60,200,192),
                        platforms.Wall(12,60,-200,192),
                        platforms.Gray_Tile_01(0,128),
                        platforms.Gray_Tile_01(8,128),
                        platforms.Gray_Tile_01(16,128),
                        platforms.Gray_Tile_01(24,128),
                        platforms.Gray_Tile_01(32,128),
                        platforms.Gray_Tile_01(40,128),
                        platforms.Gray_Tile_01(-8,96),
                        platforms.Gray_Tile_01(-16,96),
                        platforms.Gray_Tile_01(-24,96),
                        platforms.Gray_Tile_01(-32,96),]
                
        self.enemy_list = [enemies.Enemy(10, 10)]
