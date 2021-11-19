import pygame
from scripts import spritesheet

class Effect(pygame.sprite.Sprite):
    def __init__(self):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/fx.png", 1)
        self.anim = [self.sheet.get_image(0,0,1,1),
        ]
        self.surf = self.anim[0]
        self.duration: int = 0
        self.anim_speed: int = 4

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
        self.anim = [self.sheet.get_image(1,237,48,48),
            self.sheet.get_image(51,237,48,48),
            self.sheet.get_image(101,237,48,48),
            self.sheet.get_image(151,237,48,48),
            self.sheet.get_image(201,237,48,48),
            self.sheet.get_image(251,237,48,48),
            self.sheet.get_image(301,237,48,48),
        ]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.rect.center = (pos_x,pos_y)

class PlasmaShotDeath(Effect):
    def __init__(self, pos_x, pos_y):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Effect.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/projectiles.png", 1)
        self.anim = [self.sheet.get_image(1, 10, 12, 12),
                        self.sheet.get_image(15, 10, 12, 12),
                        self.sheet.get_image(29, 10, 12, 12)]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.rect.center = (pos_x,pos_y)

class MGShotDeath(Effect):
    def __init__(self, pos_x, pos_y):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Effect.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/projectiles.png", 1)
        self.anim = [self.sheet.get_image(1, 28, 5, 5),
                        self.sheet.get_image(7, 28, 5, 5),
                        self.sheet.get_image(13, 28, 5, 5)]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.rect.center = (pos_x,pos_y)

class SmallExplosion(Effect):
    def __init__(self, pos_x, pos_y):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Effect.__init__(self)
        self.anim = [self.sheet.get_image(1, 49, 16, 16),
                        self.sheet.get_image(19, 49, 16, 16),
                        self.sheet.get_image(37, 49, 16, 16),
                        self.sheet.get_image(55, 49, 16, 16),
                        self.sheet.get_image(73, 49, 16, 16),
                        self.sheet.get_image(91, 49, 16, 16),
                        self.sheet.get_image(109, 49, 16, 16),
                        self.sheet.get_image(127, 49, 16, 16)]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.rect.center = (pos_x,pos_y)

class MediumExplosion(Effect):
    def __init__(self, pos_x, pos_y):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Effect.__init__(self)
        self.anim = [self.sheet.get_image(1, 67, 22, 22),
                        self.sheet.get_image(25, 67, 22, 22),
                        self.sheet.get_image(49, 67, 22, 22),
                        self.sheet.get_image(73, 67, 22, 22),
                        self.sheet.get_image(97, 67, 22, 22),
                        self.sheet.get_image(121, 67, 22, 22),
                        self.sheet.get_image(145, 67, 22, 22),
                        self.sheet.get_image(169, 67, 22, 22)]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.rect.center = (pos_x,pos_y)

class BigExplosion(Effect):
    def __init__(self, pos_x, pos_y):
        super(Effect, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Effect.__init__(self)
        self.anim = [self.sheet.get_image(1, 91, 30, 30),
                        self.sheet.get_image(33, 91, 30, 30),
                        self.sheet.get_image(65, 91, 30, 30),
                        self.sheet.get_image(97, 91, 30, 30),
                        self.sheet.get_image(129, 91, 30, 30),
                        self.sheet.get_image(161, 91, 30, 30),
                        self.sheet.get_image(193, 91, 30, 30),
                        self.sheet.get_image(225, 91, 30, 30)]
        self.surf = self.anim[0]
        self.rect = self.surf.get_rect()
        self.rect.center = (pos_x,pos_y)