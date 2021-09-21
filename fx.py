import pygame
import spritesheet

class PlayerDeath(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(PlayerDeath, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = spritesheet.SpriteSheet("assets/sprites/fx.png", 1)
        self.anim = [self.spritesheet.get_image(1,237,48,48),
            self.spritesheet.get_image(1,237,48,48),
            self.spritesheet.get_image(51,237,48,48),
            self.spritesheet.get_image(101,237,48,48),
            self.spritesheet.get_image(151,237,48,48),
            self.spritesheet.get_image(201,237,48,48),
            self.spritesheet.get_image(251,237,48,48),
        ]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.duration = 0
        self.rect.topleft = (pos_x,pos_y)

    def update(self):
        if self.duration // 4 >= len(self.anim):
            # Once it reaches the last sprite, reset the counter
            pygame.sprite.Sprite.kill(self)
        
        self.surf = self.anim[self.duration // 4]
        self.duration += 1