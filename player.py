import pygame
import spritesheet
import globals
import projectiles
import constants

from pygame.locals import (
    KEYDOWN,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_LCTRL,
)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Player, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        # Load the sprite sheet for the player character
        self.spritesheet = spritesheet.SpriteSheet("assets/sprites/player.png", 3)
        # Set the direction the player will be facing
        self.direction = 'r'
        # Set up arrays for the sprites used for the running animations
        self.run_right = [self.spritesheet.get_image(10,60, 16,17),
                        self.spritesheet.get_image(46,60, 16,17),
                        self.spritesheet.get_image(82,60, 16,17),
                        self.spritesheet.get_image(118,60, 16,17),
                        self.spritesheet.get_image(154,60, 16,17),
                        self.spritesheet.get_image(190,60, 16,17),
                        self.spritesheet.get_image(226,60, 16,17),
                        self.spritesheet.get_image(262,60, 16,17),]

        self.run_left = [self.spritesheet.get_image(10,86, 16,17),
                        self.spritesheet.get_image(46,86, 16,17),
                        self.spritesheet.get_image(82,86, 16,17),
                        self.spritesheet.get_image(118,86, 16,17),
                        self.spritesheet.get_image(154,86, 16,17),
                        self.spritesheet.get_image(190,86, 16,17),
                        self.spritesheet.get_image(226,86, 16,17),
                        self.spritesheet.get_image(262,86, 16,17),]

        # Variable to count the frames when a movement button is being held down
        self.run_duration = 0

        # Initialize the image used for the player's sprite
        self.surf = self.spritesheet.get_image(10,8, 16, 17)
        # Initialize rect, set the starting position
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        # Set the maximum falling speed
        self.max_fall_speed = 40
        # Get the currently loaded level, used for collision detection
        self.level = None
        # Variables for movement
        self.change_x = 0
        self.change_y = 0     
        # Initialize class that's used to check if the player is on ground
        self.groundcheck = GroundCheck(self.rect.width)
        #globals.active_sprites.add(self.groundcheck)
        
    # Movement function
    def move(self, pressed_keys):

         # Check if movement keys are held down, if so, change the character's direction and move them in that direction
        if pressed_keys[K_LEFT]:
            self.change_x = -5
            self.direction = 'l'

            # Check if character is on ground. If they are, play the running animation. Otherwise switch to the jumping frame
            if self.is_grounded():
                self.run_anim()
            else:
                self.surf = self.spritesheet.get_image(46,34, 16, 17)

        # Same as above, but when moving right
        elif pressed_keys[K_RIGHT]:
            self.change_x = 5
            self.direction = 'r'
            if self.is_grounded():
                self.run_anim()
            else:
                self.surf = self.spritesheet.get_image(46,8, 16, 17)
        # When player stops moving
        else:
            self.change_x = 0
            self.run_duration = 0

            # Change to a standing sprite, depending on the direction of the player and if he's on ground or not
            if self.direction == 'r':
                if self.is_grounded():
                    # Standing sprite
                    self.surf = self.spritesheet.get_image(10,8, 16, 17)
                else:
                    # Mid-air sprite
                    self.surf = self.spritesheet.get_image(46,8, 16, 17)
            elif self.is_grounded():
                self.surf = self.spritesheet.get_image(10,34, 16, 17)
            else:
                self.surf = self.spritesheet.get_image(46,34, 16, 17)
        # Makes the player character move
        self.rect.x += self.change_x

    # Run animation function
    def run_anim(self):
        """ Use floor division to control the speed of animation
            ex: run_duration // 5 means every five frames, it advances to the next sprite of the animation"""

        if self.run_duration // 4 >= len(self.run_right):
            # Once it reaches the last sprite, reset the counter
            self.run_duration = 0

        # If character is facing right, use the right facing sprites. Otherwise use left.
        if (self.direction == 'r'):
            self.surf = self.run_right[self.run_duration // 4]
        else:
            self.surf = self.run_left[self.run_duration // 4]
        # Increase the counter by one
        self.run_duration += 1

    # Update the player character
    def update(self):

        # Get what keys are being pressed
        pressed_keys = pygame.key.get_pressed()

        # Set the ground check actor below the player character
        self.groundcheck.setpos(self.rect.x,self.rect.bottom)

        # Call the move function, pass the keypresses to it
        self.move(pressed_keys)

        self.collision_detection(pressed_keys)

        # Move the character down, to make it fall. Cap the falling speed at the maximum defined
        if(self.change_y <= self.max_fall_speed):
            self.change_y += .5
        else:
            self.change_y = self.max_fall_speed
        

    def collision_detection(self, pressed_keys):
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
                if self.rect.bottom - self.change_y < plat.rect.bottom and not pressed_keys[K_DOWN]:
                   self.rect.bottom = plat.rect.top
                   self.change_y = 0

    # Function for firing the gun
    def shoot(self):
        if self.direction == 'l':
            shotx = self.rect.left
            shotspeed = -16
        else:
            shotx = self.rect.right - 16
            shotspeed = 16
        proj = projectiles.Projectile(shotx,self.rect.centery - 4,shotspeed,0)
        proj.level = self.level
            
    # Jumping function
    def jump(self):
        # Check if the player character is on ground before allowing them to jump
        if self.is_grounded():
            self.change_y = -13

    # Function for checking if player is on ground
    def is_grounded(self):
        """ Get collision from walls and platforms, check if they collide with the ground check actor
        If there is collision, character is on ground and returns True
        Else, the character is off the ground and returns False """
        hits = pygame.sprite.spritecollide(self.groundcheck, self.level.wall_list, False)
        hits.extend(pygame.sprite.spritecollide(self.groundcheck, self.level.platform_list, False))
        if hits:
            return True

        return False
        
        
# Class to help check if the player character is on ground
class GroundCheck(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((x,4))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    def setpos(self, x, y):
        self.rect.x = x
        self.rect.y = y
