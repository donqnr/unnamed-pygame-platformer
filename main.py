import pygame
import levels
import player
import constants
import vars
import cam

from pygame.locals import (
    K_ESCAPE,
    K_PAUSE,
    KEYDOWN,
    QUIT,
)

# Function to check if a sprite is near or in the viewport
def is_onscreen(thing):
    # Apologies for this abomination of a line
    if thing.rect.centerx <= player.rect.centerx + constants.SCREEN_WIDTH and thing.rect.centerx >= player.rect.centerx - constants.SCREEN_WIDTH and thing.rect.centery <= player.rect.centery + constants.SCREEN_HEIGHT and thing.rect.centery >= player.rect.centery - constants.SCREEN_HEIGHT:
        return True

    return False

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), flags)

# Set the level to load
current_level = levels.Customlevel()


# Initialize the player class and pass the current level to it, for collision detection
player = player.Player(current_level.player_start[0],current_level.player_start[1] )
player.level = current_level

vars.active_sprites.add(current_level.wall_list) 
vars.active_sprites.add(current_level.platform_list)
vars.active_sprites.add(player)
vars.active_sprites.add(current_level.enemy_list)

for enemy in current_level.enemy_list:
    enemy.level = current_level

# Initialize the camera class
cam = cam.Cam()

# Variable to keep the main loop running
running = True

clock = pygame.time.Clock()


# Main loop
while running:

    # Set the game to run at 60 FPS
    clock.tick(constants.FRAMERATE)

    # Input handling should probably be in it's own class
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # If the key was spacebar, try to jump
            if event.key == pygame.K_SPACE and not vars.paused:
                player.jump()
            # If the key was left ctrl, try to shoot
            if event.key == pygame.K_LCTRL and not vars.paused:
                player.shoot()
            # If the key was pause, pause the game
            if event.key == pygame.K_PAUSE:
                if vars.paused:
                    vars.paused = False
                else:
                    vars.paused = True
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Draw the background of the current level
    screen.blit(current_level.background, (0,0))

    # Draw active sprites, in relation to the camera's position. Update when not paused
    for thing in vars.active_sprites:
        if is_onscreen(thing):
            screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    # Update the active sprites, unless the game is paused
    if not vars.paused:
        vars.active_sprites.update()

    # If the player gets a certain amount of distance away from the center of the screen, the camera starts following them
    if player.rect.right + cam.get_screen_center_x() > 5:
        cam.set_pos_x(player.rect.right - constants.SCREEN_WIDTH * .5 - 5)
    
    if player.rect.left + cam.get_screen_center_x() < -40:
        cam.set_pos_x(player.rect.left - constants.SCREEN_WIDTH * .5 - -40)

    if player.rect.bottom + cam.get_screen_center_y() > 15:
        cam.set_pos_y(player.rect.bottom - constants.SCREEN_HEIGHT * .5 - 15)
        
    if player.rect.top + cam.get_screen_center_y() < -30:
        cam.set_pos_y(player.rect.top - constants.SCREEN_HEIGHT * .5 - -30)

    # Update the image
    pygame.display.update()
