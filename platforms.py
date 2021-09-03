import pygame

# Test class for platforms, which allow the player to jump through them and stand on top of them
class Platform(pygame.sprite.Sprite):

    def __init__(self, size_x, size_y, pos_x, pos_y):
        super(Platform, self).__init__()
        self.surf = pygame.Surface((size_x,size_y))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

# Test class for walls, which block the player from all sides
class Wall(pygame.sprite.Sprite):

    def __init__(self, size_x, size_y, pos_x, pos_y):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((size_x,size_y))
        self.surf.fill((0, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)

class Gray_Tile_01(pygame.sprite.Sprite):
    def __init__(self):
        pass
