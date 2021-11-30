import pygame
from pygame.surface import Surface
from scripts.fx import Effect, PlasmaShotDeath, MGShotDeath, BigExplosion
from scripts import globals, spritesheet
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, direction = 'r'):
        super(Projectile, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/projectiles.png", 1)
        self.surf = self.sheet.get_image(1,1,8,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_x: float = speed_x
        self.speed_y: float = speed_y
        self.acceleration: float = 0
        self.damage: int = 8
        self.lifespan: int = 45
        self.lifetime: int = 0
        self.state: str = "spawn"
        self.explosive: bool = False
        self.explosion_radius: float = 1.5
        globals.active_sprites.add(self)
        globals.visible_sprites.add(self)
        self.deathanimtime: int = 0
        self.deathanim: Effect = PlasmaShotDeath
        self.asd: tuple = [0,0]
        self.knockback: float = 1
        self.direction = direction
        self.damage_enemies: bool = True
        self.damage_player: bool = False
        self.gravity: float = 0.0
        self.bouncy: bool = False
        self.frames: list[Surface] = [self.sheet.get_image(1,1,8,8)]
        self.anim_speed: int = 3
        self.anim_duration: int = 0

    def update(self):

        if self.anim_duration // self.anim_speed >= len(self.frames):
            self.anim_duration = 0

        if self.anim_duration // self.anim_speed < len(self.frames):
            self.surf = self.frames[self.anim_duration // self.anim_speed]
            self.anim_duration += 1

        if self.state == "spawn":
            self.spawn()
        elif self.state == "death":
            self.death()
        elif self.state == "predeath":
            self.predeath()
        else:
            pygame.sprite.Sprite.kill(self)

    def predeath(self):
        deathfx = self.deathanim(self.rect.centerx, self.rect.centery)
        globals.visible_sprites.add(deathfx)
        globals.active_sprites.add(deathfx)
        if self.explosive:
            self.blast_damage()
        self.state = "death"

    def blast_damage(self):
        hits = []
        if self.damage_enemies:
            hits += pygame.sprite.spritecollide(self, globals.enemy_sprites, False, pygame.sprite.collide_circle_ratio(self.explosion_radius))
        if self.damage_player:
            hits += pygame.sprite.spritecollide(self, globals.player_sprites, False, pygame.sprite.collide_circle_ratio(self.explosion_radius))
        for hit in hits:
            try:
                hit.takedamage(self.damage)
                if hit.rect.centerx > self.rect.centerx:
                    hit.change_x += self.knockback
                if hit.rect.centerx < self.rect.centerx:
                    hit.change_x -= self.knockback
            except AttributeError as e:
                print(e)

    def death(self):
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

        if self.bouncy:
            self.bounce()
        else:
            self.wallhit()

        hits = []
        if self.damage_enemies:
            hits += pygame.sprite.spritecollide(self, globals.enemy_sprites, False)
        if self.damage_player:
            hits += pygame.sprite.spritecollide(self, globals.player_sprites, False)
        
        if hits:
            try:
                if self.speed_x < 0:
                    hits[0].change_x -= self.knockback * hits[0].knockback_mult
                if self.speed_x > 0:
                    hits[0].change_x += self.knockback * hits[0].knockback_mult
                hits[0].takedamage(self.damage)

            except AttributeError:
                pass

            self.state = "predeath"

        if self.speed_x < 0:
            self.speed_x -= self.acceleration
        if self.speed_x > 0:
            self.speed_x += self.acceleration

        self.speed_y += self.gravity

    def wallhit(self):
        hits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        if hits:
            self.state = "predeath"

    # Bouncing function is still work-in-progress
    def bounce(self):
        trhit: bool = False
        tlhit: bool = False
        brhit: bool = False
        blhit: bool = False

        bounced: bool = False
        hits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        for hit in hits:
            if pygame.Rect.collidepoint(hit.rect,self.rect.topright):
                trhit = True
            if pygame.Rect.collidepoint(hit.rect,self.rect.topleft):
                tlhit = True
            if pygame.Rect.collidepoint(hit.rect,self.rect.bottomright):
                brhit = True
            if pygame.Rect.collidepoint(hit.rect,self.rect.bottomleft):
                blhit = True

            if trhit and brhit and self.speed_x > 0:
                self.rect.right = hits[0].rect.left
                self.speed_x -= self.speed_x * (2)
                bounced = True
            if tlhit and blhit and self.speed_x < 0:
                self.rect.left = hits[0].rect.right
                self.speed_x -= self.speed_x * (2)
                bounced = True
            if blhit and brhit:
                self.rect.bottom = hits[0].rect.top
                self.speed_y -= self.speed_y * (2)
                bounced = True
            if tlhit and trhit:
                self.rect.top = hits[0].rect.bottom
                self.speed_y -= self.speed_y * (2)
                bounced = True
            
        if bounced:
            self.speed_y -= self.speed_y * 0.2
            self.speed_x -= self.speed_x * 0.1
            
        

class PlasmaRifleShot(Projectile):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, direction = 'r'):
        super(Projectile, self).__init__()
        Projectile.__init__(self, pos_x, pos_y, speed_x, speed_y, direction)
        self.damage = 5
        self.surf = self.sheet.get_image(2,2,6,6)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.knockback = 1.5
        self.frames: list[Surface] = [self.sheet.get_image(2,2,6,6)]

class MGShot(Projectile):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, direction):
        super(Projectile, self).__init__()
        Projectile.__init__(self, pos_x, pos_y, speed_x, speed_y, direction)
        self.damage = 2
        self.surf = self.sheet.get_image(1,24,4,2)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y + 3
        self.deathanim = MGShotDeath
        self.knockback = 0.5
        self.frames: list[Surface] = [self.sheet.get_image(1,24,4,2)]

class RocketShot(Projectile):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, direction = 'r'):
        super(Projectile, self).__init__()
        Projectile.__init__(self, pos_x, pos_y, speed_x, speed_y, direction)
        self.damage = 16
        self.explosive = True
        self.surf = self.sheet.get_image(1,34,9,6)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.knockback = 3
        self.acceleration = 0.25
        self.deathanim = BigExplosion
        self.direction = direction
        self.frames: list[Surface] = [self.sheet.get_image(1,34,9,6)]
        if self.direction == 'l':
            self.surf = pygame.transform.flip(self.surf,True,False)

class Grenade(Projectile):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, direction):
        super(Projectile, self).__init__()
        Projectile.__init__(self, pos_x, pos_y, speed_x, speed_y, direction)
        self.damage = 16
        self.explosive = True
        self.surf = self.sheet.get_image(2,52,8,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.knockback = 3
        self.acceleration = -0.01
        self.deathanim = BigExplosion
        self.gravity = 0.1
        self.bouncy = True
        self.lifespan = 120
        self.frames: list[Surface] = [self.sheet.get_image(1,52,9,9),
                                    self.sheet.get_image(13,52,9,9),
                                    self.sheet.get_image(25,52,9,9),
                                    self.sheet.get_image(38,52,9,9),]

class EnemyGrenade(Projectile):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, direction):
        super(Projectile, self).__init__()
        Projectile.__init__(self, pos_x, pos_y, speed_x, speed_y, direction)
        self.damage = 16
        self.explosive = True
        self.surf = self.sheet.get_image(2,52,8,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.knockback = 3
        self.acceleration = -0.01
        self.deathanim = BigExplosion
        self.gravity = 0.1
        self.bouncy = True
        self.lifespan = 120
        self.damage_player = True
        self.damage_enemies = False
        self.frames: list[Surface] = [self.sheet.get_image(1,42,9,9),
                                    self.sheet.get_image(13,42,9,9),
                                    self.sheet.get_image(25,42,9,9),
                                    self.sheet.get_image(38,42,9,9),]