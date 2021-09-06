import pygame
import spritesheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/enemies.png", 3)
        self.surf = self.sheet.get_image(1,32,16,14)