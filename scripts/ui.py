import pygame
from scripts import constants, globals
from scripts.player import Player

class Hud(pygame.sprite.Sprite):
    def __init__(self):
        self.hp = HPBar()
        self.ammo = AmmoBar()
        self.wpn = WeaponName()
        self.msg = Message()

    def update(self):
        self.hp.update()
        self.ammo.update()
        self.wpn.update()
        self.msg.update()

    def set_player(self, player: Player):
        self.hp.player = player
        self.ammo.player = player
        self.wpn.player = player

class HPBar(pygame.sprite.Sprite):
    def __init__(self):
        self.player = None
        self.font = pygame.font.Font("assets/fonts/BULKYPIX.TTF", 16)
        self.text = self.update_counter()
        self.rect = self.text.get_rect()
        self.text.set_colorkey((0,0,0))
        self.rect.bottomleft = (8, constants.SCREEN_HEIGHT)

    def update(self):
        self.text = self.update_counter()

    def update_counter(self) -> pygame.Surface:
        try:
            return self.font.render("Health: " + str(self.player.hp), True, (255,255,255))
        except AttributeError:
            return self.font.render("", True, (255,255,255))

class AmmoBar(pygame.sprite.Sprite):
    def __init__(self):
        self.player = None
        self.font = pygame.font.Font("assets/fonts/BULKYPIX.TTF", 16)
        self.text = self.font.render("", False, (255,255,255))
        self.rect = self.text.get_rect()
        self.text.set_colorkey((0,0,0))
        self.rect.bottomleft = (constants.SCREEN_WIDTH - 120, constants.SCREEN_HEIGHT)

    def update(self):
        try:
            if self.player.equipped_weapon.ammo_consumption < 1:
                ammocounter = 'INF'
            else:
                ammocounter = str(self.player.equipped_weapon.ammo)
            self.text = self.font.render("Ammo: " + ammocounter, True, (255,255,255))
        except AttributeError:
            pass

class WeaponName(pygame.sprite.Sprite):
    def __init__(self):
        self.player = None
        self.font = pygame.font.Font("assets/fonts/BULKYPIX.TTF", 12)
        self.text = self.font.render("", False, (255,255,255))
        self.rect = self.text.get_rect()
        self.text.set_colorkey((0,0,0))
        self.rect.bottomleft = (constants.SCREEN_WIDTH - 120, constants.SCREEN_HEIGHT - 20)

    def update(self):
        try:
            self.text = self.font.render(self.player.equipped_weapon.name, True, (255,255,255))
        except AttributeError:
            pass

class Message(pygame.sprite.Sprite):
    def __init__(self):
        self.font = pygame.font.Font("assets/fonts/BULKYPIX.TTF", 12)
        self.text = self.font.render("test", False, (255,255,255))
        self.rect = self.text.get_rect()
        self.text.set_colorkey((0,0,0))
        self.rect.bottomleft = (16, 16)
        self.message_duration = 120
        self.message_counter = 0

    def show_message(self, message: str):
        self.text = self.font.render(message, False, (255,255,255))
        self.message_counter = 0

    def update(self):
        if self.message_counter >= self.message_duration:
            self.text = self.font.render("", False, (255,255,255))
        else:
            self.message_counter += 1