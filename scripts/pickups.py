from pygame import sprite
from scripts import player, spritesheet, globals
from scripts.weapons import MachineGun

class Stimpack(sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Stimpack, self).__init__()
        sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/pickups.png", 1)
        self.surf = self.sheet.get_image(31,10,14,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        globals.active_sprites.add(self)
        globals.visible_sprites.add(self)

    def update(self):
        hits = sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            try:
                if hit.hp < hit.maxhp:
                    hit.heal(15)
                    sprite.Sprite.kill(self)
                else:
                    pass
            except AttributeError:
                pass

class MGAmmo(sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(MGAmmo, self).__init__()
        sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/pickups.png", 1)
        self.surf = self.sheet.get_image(1,10,14,8)
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        globals.active_sprites.add(self)
        globals.visible_sprites.add(self)
        
    def update(self):
        hits = sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            try:
                hit.weapons[1].ammo += 50
                sprite.Sprite.kill(self)
            except (AttributeError, ValueError) as e:
                print(str(e))