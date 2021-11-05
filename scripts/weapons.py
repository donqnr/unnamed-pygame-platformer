import pygame
from projectiles import Projectile

class Weapon():
    def __init__(self):
        self.projectile_speed = [0,0]
        self.projectile = Projectile
        self.auto = False
        self.ammo = 0
        self.ammo_consumption = 0
        self.state = 'unequipped'
        self.firerate = 0
        self.fireratecooldown = 0
        self.owner = None

    def update(self):
        if not self.state == 'unequipped':
            if self.state == 'ready':
                pass
            elif self.state == 'firing' and self.fireratecooldown < 1:
                self.fire()
            else:
                self.fireratecooldown -= 1

    def triggerdown(self):
        self.state = 'firing'

    def triggerup(self):
        self.state = 'ready'

    def fire(self):
        if self.owner.direction == 'l':
            shotx = self.owner.rect.left
            shotspeed = -self.projectile_speed[0]
        else:
            shotx = self.owner.rect.right - 6
            shotspeed = self.projectile_speed[0]
        proj = self.projectile(shotx,self.owner.rect.centery - 2,shotspeed,self.projectile_speed[0])
        self.ammo -= self.ammo_consumption
        self.fireratecooldown = self.firerate
        if not self.auto:
            self.state = 'ready'

class PlasmaRifle(Weapon):
    def __init__(self):
        super().__init__()
        Weapon.__init__(self)
        self.projectile_speed = [6,0]
        self.auto = True
        self.firerate = 10