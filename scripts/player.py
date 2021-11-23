import pygame
import math

from scripts import globals, spritesheet, fx
from scripts.weapons import GrenadeLauncher, MachineGun, PlasmaRifle, RocketLauncher, Weapon

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
        self.spritesheet = spritesheet.SpriteSheet("assets/sprites/player.png", 1)
        # Set the direction the player will be facing
        self.direction: str = 'r'
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
        self.run_duration: int = 0

        # Initialize the image used for the player's sprite
        self.surf = self.spritesheet.get_image(10,8, 16, 17)

        # Initialize rect, set the starting position
        self.rect = self.surf.get_rect()
        self.rect.inflate_ip(0, -1)
        self.rect.x = pos_x
        self.rect.y = pos_y

        # Set the maximum falling speed
        self.max_fall_speed = 4.0

        # Variables for movement
        self.change_x = 0
        self.change_y = 0

        # List of weapons
        self.weapons: Weapon = [PlasmaRifle(),
                        MachineGun(),
                        RocketLauncher(),
                        GrenadeLauncher()]

        # Set the weapon's owner to the player
        for wpn in self.weapons:
            wpn.owner = self

        # Currently equipped weapon
        self.equipped_weapon: Weapon = self.weapons[0]

        # Initialize class that's used to check if the player is on ground
        self.groundcheck = GroundCheck(self.rect.width)

        # Player's health and the maximum amount 
        self.hp = 100
        self.maxhp = 100

        # Player's state
        self.state = "normal"

        # Invulnerability time, used to give a grace period after getting hit
        self.invul_time = 0

        # How many frames to wait until the player respawns after dying
        self.respawn_time = 120

        # Variable to help give a more precise control over the player's speed, dunno what name to give it
        self.asd = 0.0

        # The player's movement speed
        self.speed = 1.5

        # Add the player to the player and visible sprite groups
        globals.player_sprites.add(self)
        globals.visible_sprites.add(self)
        
    # Update the player character
    def update(self):

        # Get what keys are being pressed
        pressed_keys = pygame.key.get_pressed()

        # Set the ground check actor below the player character
        #self.groundcheck.setpos(self.rect.x,self.rect.bottom)

        if self.state == "normal":
            # Call the move function, pass the keypresses to it
            self.equipped_weapon.update()
        if self.state == "death":
            self.death()
        if self.state == "deathloop":
            self.deathloop()

        # Move the character down, to make it fall. Cap the falling speed at the maximum defined
        if(self.change_y <= self.max_fall_speed):
            self.change_y += 0.2
        else:
            self.change_y = self.max_fall_speed

        self.collision_detection(pressed_keys)

        if self.invul_time > 0 and not self.is_dead():
            self.invul_time -= 1
            if (self.invul_time % 2) == 0:
                globals.visible_sprites.add(self)
            else:
                globals.visible_sprites.remove(self)
        self.groundcheck.setpos(self.rect.x,self.rect.bottom)

    # Movement function
    def move(self, pressed_keys):
         # Check if movement keys are held down, if so, change the character's direction and move them in that direction
        if pressed_keys[K_LEFT]:
            self.change_x = -self.speed
            self.direction = 'l'

            # Check if character is on ground. If they are, play the running animation. Otherwise switch to the jumping frame
            if self.is_grounded():
                self.run_anim()
            else:
                self.surf = self.spritesheet.get_image(46,34, 16, 17)

        # Same as above, but when moving right
        elif pressed_keys[K_RIGHT]:
            self.change_x = self.speed
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

        # Make the player character move
        """ gfsdhj """
        self.asd += self.change_x - math.floor(self.change_x)
        if self.asd >= 1.0:
            self.rect.x += 1
            self.asd -= 1.0
        
        self.rect.x += math.floor(self.change_x)
        

    # Run animation function
    def run_anim(self):
        """ Use floor division to control the speed of animation
            ex: run_duration // 5 means every five frames, it advances to the next sprite of the animation"""

        if self.run_duration // 5 >= len(self.run_right):
            # Once it reaches the last sprite, reset the counter
            self.run_duration = 0

        # If character is facing right, use the right facing sprites. Otherwise use left.
        if (self.direction == 'r'):
            self.surf = self.run_right[self.run_duration // 5]
        else:
            self.surf = self.run_left[self.run_duration // 5]
        # Increase the counter by one
        self.run_duration += 1

    def collision_detection(self, pressed_keys):
        # Check for collision horizontally, prevent the character from moving through walls
        wallhits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        for wall in wallhits:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            if self.change_x < 0:
                self.rect.left = wall.rect.right

        # Using the floor function here to prevent weirdness when the player moves into negative coords
        self.rect.y += math.floor(self.change_y)

        # Check for collision vertically, prevent the character from falling or jumping through walls
        wallhits = pygame.sprite.spritecollide(self, globals.current_level.wall_list, False)
        for wall in wallhits:
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            elif self.change_y < 0:
                self.rect.top = wall.rect.bottom      
            # Stop the character falling if there's something below him
            self.change_y = 0
    
        # Check for collision on platforms, the player can move and jump through them, while being able to land and stand on top of them
        platformhits = pygame.sprite.spritecollide(self, globals.current_level.platform_list, False)
        for plat in platformhits:
            if self.change_y > 0:
                #if self.rect.bottom - self.change_y < plat.rect.bottom and not pressed_keys[K_DOWN]:
                if self.rect.bottom - self.change_y < plat.rect.top + 1 and not pressed_keys[K_DOWN]:
                   self.rect.bottom = plat.rect.top
                   self.change_y = 0

    # Function for firing the gun
    def shoot(self):
        if not self.is_dead() and self.equipped_weapon != None:
            self.equipped_weapon.triggerdown()
            
    def stopshoot(self):
        if self.equipped_weapon != None:
            self.equipped_weapon.triggerup()
        if self.equipped_weapon.ammo < 1:
            self.equipped_weapon = self.weapons[0]
        
    # Jumping function
    def jump(self):
        # Check if the player character is on ground and not dead before allowing them to jump
        if self.is_grounded() and not self.is_dead():
            self.change_y = -4

    # Function for checking if player is on ground
    def is_grounded(self):
        """ Get collision from walls and platforms, check if they collide with the ground check actor
        If there is collision, character is on ground and returns True
        Else, the character is off the ground and returns False """
        hits = pygame.sprite.spritecollide(self.groundcheck, globals.current_level.wall_list, False)
        hits.extend(pygame.sprite.spritecollide(self.groundcheck, globals.current_level.platform_list, False))
        if hits:
            return True

        return False


    # Function for player's death state
    def death(self):
        globals.visible_sprites.remove(self)
        deathfx = fx.PlayerDeath(self.rect.centerx, self.rect.centery)
        globals.visible_sprites.add(deathfx)
        globals.active_sprites.add(deathfx)
        self.state = "deathloop"

    # Function for a looping state that's called right after the death state
    def deathloop(self):
        self.respawn_time -= 1
        if self.respawn_time <= 0:
            self.respawn()

    # Function to check if the player's dead
    def is_dead(self) -> bool:
        if self.hp < 1:
            return True

        return False

    # Function to handle taking damage
    def takedamage(self, dmg):
        if not self.is_dead():
            if not self.invul_time > 0 and self.hp > 0:
                self.hp -= dmg
                self.invul_time = 60
            if self.hp <= 0:
                self.state = "death"

    # Function for making the player move without the player's input
    def push(self, x, y):
        pass

    # Function for respawning after the player dies
    def respawn(self):
        self.state = "normal"
        self.rect.topleft = globals.current_level.player_start
        globals.visible_sprites.add(self)
        self.hp = self.maxhp
        self.respawn_time = 120

    # Function for healing the player
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    # Function to handle changing weapons
    def change_weapon(self, num):
        try:
            if self.weapons[num - 1].ammo > 0:
                self.equipped_weapon = self.weapons[num - 1]
        except IndexError:
            print("No weapon at slot " + str(num))

        
        
# Class to help check if the player character is on ground
class GroundCheck(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((x,1))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        #globals.visible_sprites.add(self)

    def setpos(self, x, y):
        self.rect.x = x
        self.rect.y = y