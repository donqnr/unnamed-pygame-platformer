import pygame
import globals
import constants
import levels
import platforms
import cam

from pygame.locals import (
    K_ESCAPE,
    K_PAUSE,
    K_w,
    K_a,
    K_s,
    K_d,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

#

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.EDITOR_SCREEN_WIDTH, constants.EDITOR_SCREEN_HEIGHT), flags)

# Set the level to load
current_level = levels.TestLevel()

globals.active_sprites.add(current_level.wall_list) 
globals.active_sprites.add(current_level.platform_list)
globals.active_sprites.add(current_level.enemy_list)

# Variable to keep the main loop running
running = True

clock = pygame.time.Clock()

cam = cam.Cam()

blocklist = [platforms.Tan_Tile_01,
            platforms.Ground_Tile_01]

# Main loop
while running:


    # Set the game to run at 60 FPS
    clock.tick(constants.FRAMERATE)

    # Input handling should probably be in it's own class
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_a]:
        cam.x += 2
    if pressed_keys[K_d]:
        cam.x -= 2
    if pressed_keys[K_w]:
        cam.y += 2
    if pressed_keys[K_s]:
        cam.y -= 2
        
    screen.blit(pygame.transform.scale(current_level.background, (constants.EDITOR_SCREEN_WIDTH,constants.EDITOR_SCREEN_HEIGHT)), (0,0))

    for thing in globals.active_sprites:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    selected_block = 0

    pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] == 1:
        print(str((pos[0] - cam.x) // 8 * 8) + " " + str((pos[1] - cam.y) // 8 * 8))
        tile = blocklist[selected_block]((pos[0] - cam.x) // 8 * 8, (pos[1] - cam.y) // 8 * 8)
        globals.active_sprites.add(tile)

    if pygame.mouse.get_pressed()[2] == 1:
        print(str((pos[0] - cam.x) // 8 * 8) + " " + str((pos[1] - cam.y) // 8 * 8))
    


    pygame.display.update()
