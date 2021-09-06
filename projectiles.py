import pygame
import spritesheet
import globals

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed_x, speed_y):
        super(Projectile, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/projectiles.png", 3)
        self.surf = self.sheet.get_image(1,1,8,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.lifespan = 4 * 60
        self.lifetime = 0
        self.state = "spawn"
        self.deathanimtime = 0
        self.deathanim = [self.sheet.get_image(1, 10, 12, 12),
                        self.sheet.get_image(15, 10, 12, 12),
                        self.sheet.get_image(29, 10, 12, 12)]

    def update(self):
        if self.state == "spawn":
            self.spawn()
        else:
            self.death()
    def death(self):
        if self.deathanimtime // 4 >= len(self.deathanim):
            # Once it reaches the last sprite, kill the actor
            pygame.sprite.Sprite.kill(self)
        else:
            self.surf = self.deathanim[self.deathanimtime // 4]
            self.deathanimtime += 1
    def spawn(self):
        self.rect.x += self.speed_x
        self.lifetime += 1
        if self.lifetime >= self.lifespan:
            self.state = "death"
        hits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        for hit in hits:
            self.state = "death"


