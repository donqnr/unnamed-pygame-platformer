import pygame
import spritesheet
import globals

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
        self.max_fall_speed = 5
        globals.enemy_sprites.add(self)
        self.level = None
        self.hp = 4
        self.state = "alive"

    def update(self):
        if self.state == "alive":
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
        wallhits = pygame.sprite.spritecollide(self, self.level.wall_list, False)
        for wall in wallhits:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            if self.change_x < 0:
                self.rect.left = wall.rect.right
        
        self.rect.y += self.change_y

        # Check for collision vertically, prevent the character from falling or jumping through walls
        wallhits = pygame.sprite.spritecollide(self, self.level.wall_list, False)
        for wall in wallhits:
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            elif self.change_y < 0:
                self.rect.top = wall.rect.bottom      
            # Stop the character falling if there's something below him
            self.change_y = 0
    
        # Check for collision on platforms, the player can move and jump through them, while being able to land and stand on top of them
        platformhits = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for plat in platformhits:
            if self.change_y > 0:
                if self.rect.bottom - self.change_y < plat.rect.bottom:
                   self.rect.bottom = plat.rect.top
                   self.change_y = 0