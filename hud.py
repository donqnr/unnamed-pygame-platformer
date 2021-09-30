import pygame
import constants

class HealthMeter(pygame.sprite.Sprite):
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font("assets/fonts/MILLENNIA.TTF", 24)
        self.text = self.font.render("hp: " + str(self.player.hp), False, (255,255,255))
        self.rect = self.text.get_rect()
        self.rect.bottomleft = (16, constants.SCREEN_HEIGHT)

    def update(self):
        self.text = self.font.render("hp: " + str(self.player.hp), True, (255,255,255))