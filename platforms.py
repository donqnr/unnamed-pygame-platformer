from spritesheet import SpriteSheet
import pygame

# Test class for platforms, which allow the player to jump through them and stand on top of them
# Parent class for walls/platforms
class Wall(pygame.sprite.Sprite):

    def __init__(self, size_x, size_y, pos_x, pos_y):
        super(Wall, self).__init__()
        self.name = Wall
        self.sheet = SpriteSheet("assets/tiles/tiles.png", 1)
        self.surf = pygame.Surface((size_x,size_y))
        self.surf.fill((0, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Platform(Wall):

    def __init__(self, size_x, size_y, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self)
        self.surf = pygame.Surface((size_x,size_y))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Tan_Tile_01(Wall):
    def __init__(self, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self, 8, 8, pos_x, pos_y)
        self.name = Tan_Tile_01
        self.surf = self.sheet.get_image(0, 24 ,8 ,8)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Ground_Tile_01(Wall):
    def __init__(self, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = Ground_Tile_01
        self.surf = self.sheet.get_image(8, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Ground_Tile_02(Wall):
    def __init__(self, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = Ground_Tile_02
        self.surf = self.sheet.get_image(24, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Ground_Tile_03(Wall):
    def __init__(self, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = Ground_Tile_03
        self.surf = self.sheet.get_image(40, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Ground_Tile_04(Wall):
    def __init__(self, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = Ground_Tile_04
        self.surf = self.sheet.get_image(56, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Ground_Tile_05(Wall):
    def __init__(self, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = Ground_Tile_05
        self.surf = self.sheet.get_image(72, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Ground_Tile_06(Wall):
    def __init__(self, pos_x, pos_y):
        super(Wall, self).__init__()
        Wall.__init__(self, 16, 16, pos_x, pos_y)
        self.name = Ground_Tile_06
        self.surf = self.sheet.get_image(88, 0 ,16 ,16)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)
