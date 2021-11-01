import pygame
import math

from enemies.EnemyBase import Enemy
from scripts import globals

class Enemy_01(Enemy):
    def __init__(self, pos_x, pos_y):
        super(Enemy, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Enemy.__init__(self,pos_x,pos_y)
        self.max_speed = 1.45
        self.asd = 0
        self.direction = 'l'
        self.run_duration = 0

        self.run_left = [self.sheet.get_image(19,31,16,14),
                        self.sheet.get_image(37,31,16,14),
                        self.sheet.get_image(55,31,16,14),]

        self.run_right = [self.sheet.get_image(73,31,16,14),
                        self.sheet.get_image(91,31,16,14),
                        self.sheet.get_image(109,31,16,14),]

    def update(self):
        if self.state == "normal":
            self.wait()
        elif self.state == "death":
            self.death()
        elif self.state == "chase":
            self.chase()

        self.fall()
        self.collision_detection()
        self.deal_damage()

        hits = pygame.sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            try:
                hit.takedamage(1)
            except AttributeError:
                pass


    def wait(self):
        self.change_x = 0
        hits = pygame.sprite.spritecollide(self, globals.player_sprites, False, pygame.sprite.collide_circle_ratio(7))
        for hit in hits:
            self.state = "chase"
            self.target = hit

    def fall(self):
        # Move the character down, to make it fall. Cap the falling speed at the maximum defined
        if(self.change_y <= self.max_fall_speed):
            self.change_y += .2
        else:
            self.change_y = self.max_fall_speed
    
    def move_anim(self):

        if math.ceil(self.run_duration) // 7 >= len(self.run_right):
            # Once it reaches the last sprite, reset the counter
            self.run_duration = 0

        # If character is facing right, use the right facing sprites. Otherwise use left.
        if self.change_x >= 0.1:
            self.surf = self.run_right[math.ceil(self.run_duration) // 7]
        elif self.change_x <= -0.1:
            self.surf = self.run_left[math.ceil(self.run_duration) // 7]
        else:
            self.surf = self.sheet.get_image(1,31,16,13)
        # Increase the counter by one
        if self.change_x < 0:
            self.run_duration -= self.change_x
        else:
            self.run_duration += self.change_x
        
    def move(self):
        self.asd += self.change_x - math.floor(self.change_x)
        if self.asd >= 1.0:
            self.rect.x += 1
            self.asd -= 1.0

        self.rect.x += math.floor(self.change_x)
        self.move_anim()

    def chase(self):
        if self.target != None:
            if self.target.rect.centerx < self.rect.centerx:
                self.direction = 'l'
                if self.change_x > self.max_speed - (self.max_speed * 2):
                    self.change_x += -0.1
                else:
                    self.change_x = -self.max_speed
            elif self.target.rect.centerx > self.rect.centerx:
                self.direction = 'r'
                if self.change_x < self.max_speed:
                    self.change_x += 0.1
                else:
                    self.change_x = self.max_speed

        self.move()
        try:
            if self.target.is_dead():
                self.target = None
                self.surf = self.sheet.get_image(1,31,16,13)
                self.state = "normal"
        except AttributeError:
            pass

    def deal_damage(self):
        hits = pygame.sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            try:
                hit.takedamage(1)
            except AttributeError:
                pass