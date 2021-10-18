import pygame
import levels
import player
import constants
import vars
import cam
import hud

from pygame.locals import (
    K_ESCAPE,
    K_PAUSE,
    K_F1,
    K_F2,
    KEYDOWN,
    QUIT,
)

# Function to check if a sprite is near or in the viewport
def is_onscreen(thing):
    # Apologies for this abomination of a line
    if thing.rect.centerx <= player.rect.centerx + constants.SCREEN_WIDTH and thing.rect.centerx >= player.rect.centerx - constants.SCREEN_WIDTH and thing.rect.centery <= player.rect.centery + constants.SCREEN_HEIGHT and thing.rect.centery >= player.rect.centery - constants.SCREEN_HEIGHT:
        return True

    return False

def changelevel(level_file):
    vars.bg_sprites.empty()
    vars.enemy_sprites.empty()
    vars.visible_sprites.empty()
    vars.active_sprites.empty()
    newlevel = levels.Customlevel(level_file)
    vars.active_sprites.add(newlevel.enemy_list)
    for enemy in newlevel.enemy_list:
        enemy.level = newlevel
    return newlevel

def initplayer():
    p = player.Player(current_level.player_start[0],current_level.player_start[1])
    return p

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), flags)

# Set the level to load
current_level = changelevel("level01.json")

# Initialize the player class and pass the current level to it, for collision detection
player = initplayer()
player.level = current_level

hud = hud.Hud(player)

""" vars.active_sprites.add(current_level.wall_list) 
vars.active_sprites.add(current_level.platform_list) """
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
            if event.key == pygame.K_F1:
                current_level.destroy_level()
                current_level = changelevel("levl2.json")
                player.level = current_level
                player.rect.topleft = current_level.player_start
                vars.visible_sprites.add(player)
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False 

    # Draw the background of the current level
    screen.blit(current_level.background, (0,0))

    # Draw the background elements of the level, before any others
    for thing in vars.bg_sprites:
        if is_onscreen(thing):
            screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    # Draw visible sprites, in relation to the camera's position.
    for thing in vars.visible_sprites:
        if is_onscreen(thing):
            screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    screen.blit(hud.text, (hud.rect.x,hud.rect.y))
    hud.update()

    # Update the active sprites, unless the game is paused
    if not vars.paused:
        vars.player_sprites.update()
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
