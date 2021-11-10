import pygame
import spritesheet
from fx import PlasmaShotDeath, MGShotDeath
from scripts import globals
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed_x, speed_y):
        super(Projectile, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/projectiles.png", 1)
        self.surf = self.sheet.get_image(1,1,8,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.damage = 8
        self.lifespan = 45
        self.lifetime = 0
        self.state = "spawn"
        globals.active_sprites.add(self)
        globals.visible_sprites.add(self)
        self.deathanimtime = 0
        self.deathanim = PlasmaShotDeath
        self.asd = [0,0]

    def update(self):
        if self.state == "spawn":
            self.spawn()
        elif self.state == "death":
            self.death()
        elif self.state == "predeath":
            self.predeath()
        else:
            pygame.sprite.Sprite.kill(self)

    def predeath(self):
        self.state = "death"

    def death(self):
        deathfx = self.deathanim(self.rect.centerx, self.rect.centery)
        globals.visible_sprites.add(deathfx)
        globals.active_sprites.add(deathfx)
        pygame.sprite.Sprite.kill(self)

        """ if self.deathanimtime // 4 >= len(self.deathanim):
            pygame.sprite.Sprite.kill(self)
        else:
            self.surf = self.deathanim[self.deathanimtime // 4]
            self.deathanimtime += 1 """

    def spawn(self):

        self.asd[0] += self.speed_x - math.floor(self.speed_x)
        self.asd[1] += self.speed_y - math.floor(self.speed_y)
        if self.asd[0] >= 1.0:
            self.rect.x += 1
            self.asd[0] -= 1.0

        if self.asd[1] >= 1.0:
            self.rect.y += 1
            self.asd[1] -= 1.0

        self.rect.x += math.floor(self.speed_x)
        self.rect.y += math.floor(self.speed_y)
        self.lifetime += 1
        if self.lifetime >= self.lifespan:
            self.state = "predeath"
        
        hits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        if hits:
            self.state = "predeath"

        hits = pygame.sprite.spritecollide(self, globals.enemy_sprites, False)
        if hits:
            try:
                hits[0].takedamage(self.damage)
            except AttributeError:
                pass
            self.state = "predeath"

class PlasmaRifleShot(Projectile):
    def __init__(self, pos_x, pos_y, speed_x, speed_y):
        super(Projectile, self).__init__()
        Projectile.__init__(self, pos_x, pos_y, speed_x, speed_y)
        self.surf = self.sheet.get_image(2,2,6,6)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

class MGShot(Projectile):
    def __init__(self, pos_x, pos_y, speed_x, speed_y):
        super(Projectile, self).__init__()
        Projectile.__init__(self, pos_x, pos_y, speed_x, speed_y)
        self.damage = 4
        self.surf = self.sheet.get_image(1,24,4,2)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y + 3
        self.deathanim = MGShotDeath
        