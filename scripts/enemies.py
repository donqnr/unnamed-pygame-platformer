import pygame
from scripts import globals, spritesheet
import math

from scripts.projectiles import EnemyGrenade

# A lot of code copied from the player class, could refactor these and have them be a child of a more general character class

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Enemy, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/enemies2.png", 1)
        self.surf = self.sheet.get_image(1,31,16,13)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.change_y = 0
        self.change_x = 0
        self.max_speed = 1
        self.max_fall_speed = 5
        globals.enemy_sprites.add(self)
        globals.visible_sprites.add(self)
        self.hp = 20
        self.state = "normal"
        self.target = None
        self.run_duration = 0
        self.knockback_mult = 1

        self.run_left = [self.sheet.get_image(1,31,16,13),]
        self.run_right = [self.sheet.get_image(1,31,16,13),]
        self.still_frame = self.sheet.get_image(1,31,16,13)

    def update(self):
        if self.state == "normal":
            self.alive()
        elif self.state == "death":
            self.death()

    def takedamage(self, dmg_amount):
        self.hp -= dmg_amount
        if self.hp < 1:
            self.state = "death"

    def alive(self):
        # Move the character down, to make it fall. Cap the falling speed at the maximum defined
        if(self.change_y <= self.max_fall_speed):
            self.change_y += .2
        else:
            self.change_y = self.max_fall_speed

        self.collision_detection()

    def death(self):
        pygame.sprite.Sprite.kill(self)

    def collision_detection(self):
        # Check for collision horizontally, prevent the character from moving through walls
        wallhits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        for wall in wallhits:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            if self.change_x < 0:
                self.rect.left = wall.rect.right
        
        self.rect.y += self.change_y

        # Check for collision vertically, prevent the character from falling or jumping through walls
        wallhits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        for wall in wallhits:
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            elif self.change_y < 0:
                self.rect.top = wall.rect.bottom      
            # Stop the character falling if there's something below him
            self.change_y = 0
    
        # Check for collision on platforms, the character can move and jump through them, while being able to land and stand on top of them
        platformhits = pygame.sprite.spritecollide(self, globals.current_level.platform_list, False)
        for plat in platformhits:
            if self.change_y > 0:
                if self.rect.bottom - self.change_y < plat.rect.bottom:
                   self.rect.bottom = plat.rect.top
                   self.change_y = 0

    def fall(self):
        # Move the character down, to make it fall. Cap the falling speed at the maximum defined
        if(self.change_y <= self.max_fall_speed):
            self.change_y += .2
        else:
            self.change_y = self.max_fall_speed

    def move(self):
        self.asd += self.change_x - math.floor(self.change_x)
        if self.asd >= 1.0:
            self.rect.x += 1
            self.asd -= 1.0

        self.rect.x += math.floor(self.change_x)
        self.move_anim()

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
            self.surf = self.still_frame
        # Increase the counter by one
        if self.change_x < 0:
            self.run_duration -= self.change_x
        else:
            self.run_duration += self.change_x

class Enemy_01(Enemy):
    def __init__(self, pos_x, pos_y):
        super(Enemy, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Enemy.__init__(self,pos_x,pos_y)
        self.max_speed = 1.2
        self.asd = 0
        self.direction = 'l'
        self.run_duration = 0

        self.sheet.get_image(1,31,16,13)

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

        """ hits = pygame.sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            try:
                hit.takedamage(1)
            except AttributeError:
                pass """


    def wait(self):
        self.change_x = 0
        hits = pygame.sprite.spritecollide(self, globals.player_sprites, False, pygame.sprite.collide_circle_ratio(7))
        for hit in hits:
            self.state = "chase"
            self.target = hit

    def chase(self):
        try:
            if self.target.is_dead():
                self.target = None
                self.surf = self.sheet.get_image(1,31,16,13)
                self.state = "normal"
        except AttributeError:
            pass

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

    def deal_damage(self):
        hits = pygame.sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            try:
                hit.takedamage(20)
            except AttributeError:
                pass
        
class GrenadeEnemy(Enemy):
    from scripts.projectiles import EnemyGrenade
    def __init__(self, pos_x, pos_y):
        super(Enemy, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        Enemy.__init__(self,pos_x,pos_y)
        self.max_speed = 0.6
        self.asd = 0
        self.direction = 'l'
        self.run_duration = 0
        self.surf = self.sheet.get_image(1,279,16,20)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.fire_cooldown = 90
        self.fire_cd_counter = 0
        self.still_frame = self.sheet.get_image(1,279,16,20)

        self.attack_anim_speed = 6
        self.attack_anim_duration = 0

        self.run_left = [self.sheet.get_image(1,279,16,20),
                         self.sheet.get_image(19,279,16,20),
                         self.sheet.get_image(37,279,16,20),
                         self.sheet.get_image(55,279,16,20),
                         self.sheet.get_image(73,279,16,20),
                         self.sheet.get_image(91,279,16,20),]

        self.run_right = [self.sheet.get_image(1,323,16,20),
                        self.sheet.get_image(19,323,16,20),
                        self.sheet.get_image(37,323,16,20),
                        self.sheet.get_image(55,323,16,20),
                        self.sheet.get_image(73,323,16,20),
                        self.sheet.get_image(91,323,16,20),]

        self.attack_left = [self.sheet.get_image(1,301,16,20),
                            self.sheet.get_image(19,301,16,20),
                            self.sheet.get_image(37,301,16,20),
                            self.sheet.get_image(55,301,16,20),]

        self.attack_right = [self.sheet.get_image(1,345,16,20),
                            self.sheet.get_image(19,345,16,20),
                            self.sheet.get_image(37,345,16,20),
                            self.sheet.get_image(55,345,16,20),]

        

    def update(self):

        self.fall()
        self.collision_detection()

        if self.fire_cd_counter > 0:
            self.fire_cd_counter -= 1

        if self.state == "normal":
            self.wait()
        elif self.state == "death":
            self.death()
        elif self.state == "chase":
            self.chase()
        elif self.state == "attack":
            self.attack()
        elif self.state == "attackanim":
            self.attackanim()
                   
    def wait(self):
        self.change_x = 0
        hits = pygame.sprite.spritecollide(self, globals.player_sprites, False, pygame.sprite.collide_circle_ratio(7))
        for hit in hits:
            self.state = "chase"
            self.target = hit

    def chase(self):
        try:
            if self.target.is_dead():
                self.target = None
                self.surf = self.sheet.get_image(1,31,16,13)
                self.state = "normal"
        except AttributeError:
            pass

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

        if pygame.sprite.spritecollide(self, globals.player_sprites, False, pygame.sprite.collide_circle_ratio(7)) and self.fire_cd_counter <= 0:
            self.state = "attackanim"

        self.move()

    def attack(self):
        if self.fire_cd_counter <= 0:
            if self.direction == 'r':
                proj = EnemyGrenade(self.rect.centerx, self.rect.centery, 2, -1.5, self.direction)
            elif self.direction == 'l':
                proj = EnemyGrenade(self.rect.centerx, self.rect.centery, -2, -1.5, self.direction)
            self.fire_cd_counter = self.fire_cooldown

    def attackanim(self):
        anim = []

        if (self.direction == 'r'):
            anim = self.attack_right
        elif (self.direction == 'l'):
            anim = self.attack_left

        if self.attack_anim_duration // self.attack_anim_speed >= len(anim):
            # Once it reaches the last sprite, reset counter and set state back to chase
            self.attack_anim_duration = 0
            self.state = "chase"

        if self.attack_anim_duration // self.attack_anim_speed < len(anim):
            if self.attack_anim_duration // self.attack_anim_speed == 2:
                self.attack()
            self.surf = anim[self.attack_anim_duration // self.attack_anim_speed]
            self.attack_anim_duration += 1

