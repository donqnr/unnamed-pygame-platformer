import pygame
import platforms
import enemies


""" Classes for everything placed in a level
Platforms, enemies, pickups and such """

class Tan_Tile_01(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 24 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_01"
        self.type = "wall"

class Ground_Tile_01(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = "Ground_Tile_01"
        self.surf = self.sheet.get_image(8, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.type = "wall"

class Ground_Tile_02(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = "Ground_Tile_02"
        self.surf = self.sheet.get_image(24, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.type = "wall"

class Ground_Tile_03(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = "Ground_Tile_03"
        self.surf = self.sheet.get_image(40, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.type = "wall"

class Ground_Tile_04(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = "Ground_Tile_04"
        self.surf = self.sheet.get_image(56, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.type = "wall"

class Ground_Tile_05(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = "Ground_Tile_05"
        self.surf = self.sheet.get_image(72, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.type = "wall"

class Ground_Tile_06(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = "Ground_Tile_06"
        self.surf = self.sheet.get_image(88, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.type = "wall"

class TestEnemy(enemies.Enemy):
    def __init__(self, pos_x, pos_y):
        super(enemies.Enemy, self).__init__()
        enemies.Enemy.__init__(self,pos_x,pos_y)
        self.name = "TestEnemy"
        self.type = "enemy"