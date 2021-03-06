import sys
import pygame
import json

from scripts import constants, globals, platforms, things
from scripts.triggers import LevelEnd

class Level():
    """ Super-class for levels, each level is a child class of this """
    def __init__(self):

        # Set up lists for platform, walls, enemies etc.
        self.platform_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.bg_list = pygame.sprite.Group()
        self.pickup_list = pygame.sprite.Group()
        self.trigger_list = pygame.sprite.Group()
        self.player_start = (0,0)
        # Set the background image for the level
        self.background = pygame.transform.scale(pygame.image.load("assets/bg/bg1.png"),(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
        # Set which level comes next
        self.nextlevel = None
        # Will the player spawn in the level? (True for a playable level, False for menu background, cutscenes etc.)
        self.spawnplayer = True

    def build_level(self, level_file):
        with open(level_file, 'r') as file:
            data = json.load(file)
            for block, pos, thingtype in data:
                thing = getattr(things, block)(pos[0],pos[1])
                thing.type = thingtype
                if thing.type == "bg":
                    self.bg_list.add(thing)
                    globals.bg_sprites.add(thing)
                elif thing.type == "wall":
                    self.wall_list.add(thing)
                    globals.visible_sprites.add(thing)
                elif thing.type == "platform":
                    self.platform_list.add(thing)
                    globals.visible_sprites.add(thing)
                elif thing.type == "enemy":
                    self.enemy_list.add(thing)
                    globals.visible_sprites.add(thing)
                elif thing.type == "pickup":
                    self.pickup_list.add(thing)
                    globals.visible_sprites.add(thing)
                elif thing.type == "pickup":
                    self.trigger_list.add(thing)
                    globals.visible_sprites.add(thing)
    
    def destroy_level(self):
        self.bg_list.empty()
        self.wall_list.empty()
        self.platform_list.empty()
        self.enemy_list.empty()
        self.pickup_list.empty()
        self.trigger_list.empty()

class TestLevel(Level):
    def __init__(self):
        Level.__init__(self)
        super(Level, self).__init__()

        self.background = pygame.transform.scale(pygame.image.load("assets/bg/bg1.png"),(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
        self.player_start = (0, 50)

        self.platform_list = [
                            things.Tan_Tile_01(48,128),
                            things.Tan_Tile_01(56,128),
                            things.Tan_Tile_01(64,128),
                            things.Tan_Tile_01(72,128),]
        
        self.wall_list = [platforms.Wall(400,10,-200,176),
                        platforms.Wall(12,60,200,192),
                        platforms.Wall(12,60,-200,192),
                        things.Tan_Tile_01(0,0),
                        things.Tan_Tile_01(0,128),
                        things.Tan_Tile_01(8,128),
                        things.Tan_Tile_01(16,128),
                        things.Tan_Tile_01(24,128),
                        things.Tan_Tile_01(32,128),
                        things.Tan_Tile_01(40,128),
                        things.Tan_Tile_01(-8,96),
                        things.Tan_Tile_01(-16,96),
                        things.Tan_Tile_01(-24,96),
                        things.Tan_Tile_01(-32,96),]
                
        self.enemy_list = [things.Enemy_01(10, 10)]

class BlankLevel(Level):
    def __init__(self):
        Level.__init__(self)
        super(Level, self).__init__()

class Customlevel(Level):
    def __init__(self, level_file):
        Level.__init__(self)
        super(Level, self).__init__()

        self.build_level(level_file)

class Level01(Level):
    def __init__(self):
        Level.__init__(self)
        super(Level, self).__init__()

        self.build_level('level01.json')

class Level02(Level):
    def __init__(self):
        Level.__init__(self)
        super(Level, self).__init__()

        self.build_level('level02.json')
        self.background = pygame.transform.scale(pygame.image.load("assets/bg/bg2.png"),(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

