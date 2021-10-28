from spritesheet import SpriteSheet
import pygame
# Test class for platforms, which allow the player to jump through them and stand on top of them
# Parent class for walls/platforms
class Wall(pygame.sprite.Sprite):

    def __init__(self, size_x, size_y, pos_x, pos_y):
        super(Wall, self).__init__()
        self.name = "Wall"
        self.sheet = SpriteSheet("assets/tiles/tilestemp.png", 1)
        self.surf = pygame.Surface((size_x,size_y))
        self.surf.fill((0, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos_x,pos_y)


