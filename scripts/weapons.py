import pygame
from scripts.projectiles import MGShot, PlasmaRifleShot, Projectile
from scripts import globals
from random import random
# 

class Weapon():
    def __init__(self):
        # Speed of the projectile in x axis, then y axis
        self.projectile_speed: tuple = [0.0,0.0]
        # The projectile class the weapon fires
        self.projectile: Projectile = PlasmaRifleShot
        # Is the weapon automatic and keeps firing when the trigger is held down?
        self.auto: bool = False
        # Amount of ammo left in the weapon
        self.ammo = 1
        # How much ammo the weapon takes per shot
        self.ammo_consumption = 0
        # State of the weapon
        self.state = 'unequipped'
        # Time between shots, 0 = can shoot every frame, 10 = shoots every 10 frames and so on
        self.firerate = 0
        # A counter to handle the weapons firerate
        self.fireratecooldown = 0
        # The owner of the weapon
        self.owner = None
        # Muzzleflash class
        self.mflash = MuzzleFlash(self)
        self.bullet_spread = 0
        self.name = "wpedssdfcdfsdfs"
        
    # Update the weapon based on its state
    def update(self):
        # If weapon is unequipped, do nothing
        if not self.state == 'unequipped':
            # Ready state is when the weapon is ready to fire
            if self.state == 'ready':
                pass
            # Firing state calls the fire function, if enough time has passed when it was last fired
            elif self.state == 'firing' and self.fireratecooldown < 1:
                self.fire()
            # Otherwise lower the cooldown variable, until it's 0
            else:
                self.fireratecooldown -= 1

    # When player holds down the trigger, change to firing state
    def triggerdown(self):
        self.state = 'firing'

    # When player releases the trigger, change back to ready state
    def triggerup(self):
        self.state = 'ready'

    # Function to handle projectile spawning and such when the weapon fires
    def fire(self):
        if self.ammo > 0:
            self.mflash.flash(2) # Call the muzzleflash to appear
            if self.owner.direction == 'l': # Set the projectile speed depending on the player's direction
                shotx = self.owner.rect.left
                shotspeed = -self.projectile_speed[0]
            else:
                shotx = self.owner.rect.right - 6
                shotspeed = self.projectile_speed[0]
            proj = self.projectile(shotx,self.owner.rect.centery - 2,shotspeed,self.projectile_speed[1] + (self.bullet_spread * (random() - random()))) # Spawn the projectile
            self.ammo -= self.ammo_consumption # Subtract ammo by the specified amount
            self.fireratecooldown = self.firerate # Add a cooldown before the weapon can be fired again
            if not self.auto: # If the weapon isn't automatic, set state to ready regardless if the trigger is held down
                self.state = 'ready'

# Plasma Rifle, the starting weapon, which is relatively weak but doesn't consume any ammo

class PlasmaRifle(Weapon):
    def __init__(self):
        super().__init__()
        Weapon.__init__(self)
        self.projectile_speed = [6.0,0.0]
        self.auto = False
        self.firerate = 3
        self.name = "Plasma Rifle"

# Machine Gun, automatic rapid-fire weapon

class MachineGun(Weapon):
    def __init__(self):
        super().__init__()
        Weapon.__init__(self)
        self.projectile = MGShot
        self.projectile_speed = [10.5,0]
        self.auto = True
        self.firerate = 3
        self.ammo = 0
        self.max_ammo = 100
        self.ammo_consumption = 1
        self.bullet_spread = 0.5
        self.name = "Machine Gun"

class MuzzleFlash(pygame.sprite.Sprite):
    def __init__(self, owner):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("assets/sprites/muzzleflash.png").convert_alpha()
        self.right = self.surf
        self.left = pygame.transform.flip(self.surf, True, False)
        self.rect = self.surf.get_rect()
        self.counter = 0
        self.duration = 0
        self.weapon = owner

    def flash(self, dur):
        self.setpos()
        globals.visible_sprites.add(self)
        globals.active_sprites.add(self)
        self.duration = dur
        self.counter = 0

    def update(self):
        self.setpos()
        self.counter += 1
        if self.counter > self.duration:
            pygame.sprite.Sprite.kill(self)

    def setpos(self):
        self.rect.y = self.weapon.owner.rect.centery - 4
        if self.weapon.owner.direction == 'l':
            self.surf = self.left
            self.rect.right = self.weapon.owner.rect.left
        else:
            self.surf = self.right
            self.rect.left = self.weapon.owner.rect.right
