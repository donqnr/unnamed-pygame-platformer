import pygame
import spritesheet

class Effect(pygame.sprite.Sprite):
    def __init__(self):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = spritesheet.SpriteSheet("assets/sprites/fx.png", 1)
        self.anim = [self.spritesheet.get_image(0,0,1,1),
        ]
        self.surf = self.anim[0]
        self.duration = 0
        self.anim_speed = 4

    def update(self):
        if self.duration // self.anim_speed >= len(self.anim):
            # Once it reaches the last sprite, kill the sprite
            pygame.sprite.Sprite.kill(self)

        if self.duration // self.anim_speed < len(self.anim):
            self.surf = self.anim[self.duration // self.anim_speed]
            self.duration += 1

class PlayerDeath(Effect):
    def __init__(self, pos_x, pos_y):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Effect.__init__(self)
        self.anim = [self.spritesheet.get_image(1,237,48,48),
            self.spritesheet.get_image(51,237,48,48),
            self.spritesheet.get_image(101,237,48,48),
            self.spritesheet.get_image(151,237,48,48),
            self.spritesheet.get_image(201,237,48,48),
            self.spritesheet.get_image(251,237,48,48),
            self.spritesheet.get_image(301,237,48,48),
        ]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.rect.center = (pos_x,pos_y)