import pygame
from scripts import globals, levels
from scripts.levels import Level02

from pygame.locals import (
    K_ESCAPE,
    K_PAUSE,
    K_F1,
    K_F2,
    K_F12,
    K_1,
    K_2,
    K_3,
    K_4,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_LEFT,
    K_RIGHT,
)

from scripts.player import Player


class InputHandler():

    def __init__(self):
        super(InputHandler, self).__init__()
        self.player: Player = None

    def CheckInput(self):

        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # If the key was spacebar, try to jump

                # If the key was pause, pause the game
                if event.key == pygame.K_PAUSE:
                    if globals.paused:
                        globals.paused = False
                    else:
                        globals.paused = True
                if event.key == pygame.K_F1:
                    nextlevel = levels.Level02()
                    globals.current_level.destroy_level()
                    globals.current_level = globals.changelevel(nextlevel)

                    """ player.rect.topleft = globals.current_level.player_start
                    globals.visible_sprites.add(player) """
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    globals.running = False
                if event.key == K_F12:
                    if globals.hide_hud:
                        globals.hide_hud = False
                    elif not globals.hide_hud:
                        globals.hide_hud = True


                # ///////////////
                # Player controls
                # ///////////////
                if not globals.paused and not self.player.is_dead():
                    # Error check in case the player class isn't passed properly
                    try:
                        # If the key was spacebar, try to jump
                        if event.key == pygame.K_SPACE:
                            self.player.jump()
                        # When left ctrl is held down, start shooting
                        if event.key == pygame.K_LCTRL:
                            self.player.shoot()     
                        if event.key == pygame.K_1:    
                            self.player.change_weapon(1)
                        if event.key == pygame.K_2:
                            self.player.change_weapon(2)
                        if event.key == pygame.K_3:
                            self.player.change_weapon(3)
                        if event.key == pygame.K_4:
                            self.player.change_weapon(4)
                    except AttributeError:
                        print("ERROR: Player not set properly in the input handler")
            if not globals.paused:
                if event.type == KEYUP:
                    # When left ctrl is not held down, stop shooting
                    try:
                        if event.key == pygame.K_LCTRL:
                            self.player.stopshoot()
                    except AttributeError:
                        pass
        pressed_keys = pygame.key.get_pressed()
        if not globals.paused and not self.player.is_dead():
            self.player.move(pressed_keys)