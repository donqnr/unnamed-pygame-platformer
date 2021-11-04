from weapons.weaponbase import Weapon


from weapons import weaponbase

class PlasmaRifle(Weapon):
    def __init__(self):
        super().__init__()
        Weapon.__init__(self)
        self.projectile_speed = [6,0]