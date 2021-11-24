import pygame
from scripts import platforms


""" Classes that are used to place things like walls, enemies, pickups and such with a level editor, and also when building a level """

class Tan_Tile_01(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 24 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_01"
        self.type = "wall"

class Tan_Tile_01_B(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(184, 0 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_01_B"
        self.type = "wall"

class Tan_Tile_02(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(8, 24 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_02"
        self.type = "wall"

class Tan_Tile_02_B(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(192, 0 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_02_B"
        self.type = "wall"

class Tan_Tile_03(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(16, 24 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_03"
        self.type = "wall"

class Tan_Tile_03_B(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(200, 0 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_03_B"
        self.type = "wall"

class Tan_Tile_04(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(24, 24 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_04"
        self.type = "wall"

class Tan_Tile_04_B(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(208, 0 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Tile_04_B"
        self.type = "wall"

class Tan_Pipe_01(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 32 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Pipe_01"
        self.type = "wall"

class Tan_Pipe_02(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(8, 32 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Pipe_02"
        self.type = "wall"

class Tan_Pipe_03(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(16, 32 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Pipe_03"
        self.type = "wall"

class Tan_Pipe_04(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 40 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Pipe_04"
        self.type = "wall"

class Tan_Pipe_05(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(8, 40 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Pipe_05"
        self.type = "wall"

class Tan_Pipe_06(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(16, 40 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Pipe_06"
        self.type = "wall"

class Tan_Pipe_07(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 48 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Pipe_07"
        self.type = "wall"

class Tan_Panel_TL(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 56 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_TL"
        self.type = "wall"

class Tan_Panel_T(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(8, 56 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_T"
        self.type = "wall"

class Tan_Panel_TR(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(16, 56 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_TR"
        self.type = "wall"

class Tan_Panel_L(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 64 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_L"
        self.type = "wall"

class Tan_Panel_M(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(8, 64 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_M"
        self.type = "wall"

class Tan_Panel_R(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(16, 64 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_R"
        self.type = "wall"

class Tan_Panel_BL(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(0, 72 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_BL"
        self.type = "wall"

class Tan_Panel_B(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(8, 72 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_B"
        self.type = "wall"

class Tan_Panel_BR(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(16, 72 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Tan_Panel_BR"
        self.type = "wall"

class Pipe_Y_01(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(48, 40 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Pipe_Y_01"
        self.type = "wall"

class Pipe_Y_01_B(platforms.Wall):
    def __init__(self, pos_x, pos_y):
        super(platforms.Wall, self).__init__()
        platforms.Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.surf = self.sheet.get_image(232, 16 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
        self.name = "Pipe_Y_01_B"
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

from scripts.enemies import Enemy_01, GrenadeEnemy
class Enemy_01(Enemy_01):
    def __init__(self, pos_x, pos_y):
        super(Enemy_01, self).__init__(pos_x,pos_y)
        self.name = "Enemy_01"
        self.type = "enemy"

class GrenadeEnemy(GrenadeEnemy):
    def __init__(self, pos_x, pos_y):
        super(GrenadeEnemy, self).__init__(pos_x,pos_y)
        self.name = "GrenadeEnemy"
        self.type = "enemy"

from scripts.pickups import MGAmmo, Stimpack, RocketAmmo, GrenadeAmmo
class MGAmmo(MGAmmo):
    def __init__(self, pos_x, pos_y):
        super(MGAmmo, self).__init__(pos_x,pos_y)
        self.name = "MGAmmo"
        self.type = "pickup"

class Stimpack(Stimpack):
    def __init__(self, pos_x, pos_y):
        super(Stimpack, self).__init__(pos_x,pos_y)
        self.name = "Stimpack"
        self.type = "pickup"

class RocketAmmo(RocketAmmo):
    def __init__(self, pos_x, pos_y):
        super(RocketAmmo, self).__init__(pos_x,pos_y)
        self.name = "RocketAmmo"
        self.type = "pickup"

class GrenadeAmmo(GrenadeAmmo):
    def __init__(self, pos_x, pos_y):
        super(GrenadeAmmo, self).__init__(pos_x,pos_y)
        self.name = "GrenadeAmmo"
        self.type = "pickup"
