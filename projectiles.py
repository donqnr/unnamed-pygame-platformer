import pygame
import spritesheet
from scripts import globals

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
        self.damage = 1
        self.lifespan = 45
        self.lifetime = 0
        self.state = "spawn"
        globals.active_sprites.add(self)
        globals.visible_sprites.add(self)
        self.deathanimtime = 0
        self.deathanim = [self.sheet.get_image(1, 10, 12, 12),
                        self.sheet.get_image(15, 10, 12, 12),
                        self.sheet.get_image(29, 10, 12, 12)]

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
        self.rect.x -= 4
        self.rect.y -= 4
        self.state = "death"

    def death(self):
        if self.deathanimtime // 4 >= len(self.deathanim):
            pygame.sprite.Sprite.kill(self)
        else:
            self.surf = self.deathanim[self.deathanimtime // 4]
            self.deathanimtime += 1

    def spawn(self):
        self.rect.x += self.speed_x
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
        Projectile.__init__(pos_x, pos_y, speed_x, speed_y)
        