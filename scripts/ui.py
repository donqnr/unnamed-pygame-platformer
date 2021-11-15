import pygame
from scripts import constants, globals

class Hud(pygame.sprite.Sprite):
    def __init__(self, player):
        self.hp = HPBar(player)
        self.ammo = AmmoBar(player)
        self.wpn = WeaponName(player)

    def update(self):
        self.hp.update()
        self.ammo.update()
        self.wpn.update()

class HPBar(pygame.sprite.Sprite):
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font("assets/fonts/BULKYPIX.TTF", 16)
        self.text = self.update_counter()
        self.rect = self.text.get_rect()
        self.text.set_colorkey((0,0,0))
        self.rect.bottomleft = (8, constants.SCREEN_HEIGHT)

    def update(self):
        self.text = self.update_counter()

    def update_counter(self) -> pygame.Surface:
        return self.font.render("Health: " + str(self.player.hp), True, (255,255,255))

class AmmoBar(pygame.sprite.Sprite):
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font("assets/fonts/BULKYPIX.TTF", 16)
        self.text = self.font.render("", False, (255,255,255))
        self.rect = self.text.get_rect()
        self.text.set_colorkey((0,0,0))
        self.rect.bottomleft = (constants.SCREEN_WIDTH - 120, constants.SCREEN_HEIGHT)

    def update(self):
        if self.player.equipped_weapon.ammo_consumption < 1:
            ammocounter = 'INF'
        else:
            ammocounter = str(self.player.equipped_weapon.ammo)
        self.text = self.font.render("Ammo: " + ammocounter, True, (255,255,255))

class WeaponName(pygame.sprite.Sprite):
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font("assets/fonts/BULKYPIX.TTF", 12)
        self.text = self.font.render("", False, (255,255,255))
        self.rect = self.text.get_rect()
        self.text.set_colorkey((0,0,0))
        self.rect.bottomleft = (constants.SCREEN_WIDTH - 120, constants.SCREEN_HEIGHT - 20)

    def update(self):
        self.text = self.font.render(self.player.equipped_weapon.name, True, (255,255,255))
