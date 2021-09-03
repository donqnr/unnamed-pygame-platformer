import pygame
import spritesheet

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed_x, speed_y):
        super(Projectile, self).__init__()
        self.sheet = spritesheet.SpriteSheet("assets/sprites/projectiles.png")
        self.surf = self.sheet.get_image(2,2,6,6)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x


