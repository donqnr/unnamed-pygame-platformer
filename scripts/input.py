import pygame
from scripts import globals

from pygame.locals import (
    K_ESCAPE,
    K_PAUSE,
    K_F1,
    K_F2,
    KEYDOWN,
    KEYUP,
    QUIT,
)

class InputHandler():

    def __init__(self):
        super(InputHandler, self).__init__()
        self.player = None

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
                """ if event.key == pygame.K_F1:
                    globals.current_level.destroy_level()
                    globals.current_level = changelevel("levl2.json")

                    player.rect.topleft = globals.current_level.player_start
                    globals.visible_sprites.add(player) """
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    globals.running = False
                # Error check in case the player class isn't passed properly
                try:
                    # If the key was spacebar, try to jump
                    if event.key == pygame.K_SPACE and not globals.paused:
                        self.player.jump()
                    # When left ctrl is held down, start shooting
                    if event.key == pygame.K_LCTRL and not globals.paused:
                        self.player.shoot()
                except AttributeError:
                    print("ERROR: Player not set properly in the input handler")

            if event.type == KEYUP:
                # When left ctrl is not held down, stop shooting
                if event.key == pygame.K_LCTRL and not globals.paused:
                    self.player.stopshoot()
