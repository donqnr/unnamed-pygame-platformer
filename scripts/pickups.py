from pygame import sprite
from scripts import player, spritesheet, globals
from scripts.weapons import MachineGun

class Pickup(sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Pickup, self).__init__()
        sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/pickups.png", 1)
        self.surf = self.sheet.get_image(31,10,14,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.message:str = "Got a pickup"
        globals.active_sprites.add(self)
        globals.visible_sprites.add(self)

    def update(self):
        hits = sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            self.do_effect(hits[0])

    def do_effect(self, hit):
        pass

class Stimpack(Pickup):
    def __init__(self, pos_x, pos_y):
        super(Pickup, self).__init__()
        sprite.Sprite.__init__(self)
        Pickup.__init__(self,pos_x,pos_y)
        self.surf = self.sheet.get_image(31,10,14,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.message = "Health +20"

    def do_effect(self, hit):
        try:
            if hit.hp < hit.maxhp:
                hit.heal(20)
                globals.hud.msg.show_message(self.message)
                sprite.Sprite.kill(self)
            else:
                pass
        except AttributeError:
                pass

class MGAmmo(Pickup):
    def __init__(self, pos_x, pos_y):
        super(Pickup, self).__init__()
        sprite.Sprite.__init__(self)
        Pickup.__init__(self,pos_x,pos_y)
        self.surf = self.sheet.get_image(1,10,14,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.message = "MG Rounds +20"
        
    def do_effect(self, hit):
        try:
            if hit.weapons[1].ammo < hit.weapons[1].max_ammo:
                hit.weapons[1].ammo += 20
                    
                if hit.weapons[1].ammo > hit.weapons[1].max_ammo:
                    hit.weapons[1].ammo = hit.weapons[1].max_ammo

                globals.hud.msg.show_message(self.message)
                sprite.Sprite.kill(self)
                
        except (AttributeError, ValueError) as e:
            print(str(e))

class RocketAmmo(Pickup):
    def __init__(self, pos_x, pos_y):
        super(Pickup, self).__init__()
        sprite.Sprite.__init__(self)
        Pickup.__init__(self,pos_x,pos_y)
        self.surf = self.sheet.get_image(1,19,14,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.message = "Rockets +2"

    def do_effect(self, hit):
        try:
            if hit.weapons[2].ammo < hit.weapons[2].max_ammo:
                hit.weapons[2].ammo += 2
                    
                if hit.weapons[2].ammo > hit.weapons[2].max_ammo:
                    hit.weapons[2].ammo = hit.weapons[2].max_ammo

                globals.hud.msg.show_message(self.message)
                sprite.Sprite.kill(self)

        except (AttributeError, ValueError) as e:
            print(str(e))