import pygame
import levels
import player
import constants
from scripts import globals, input
import cam
import hud

# Function to check if a sprite is near or in the viewport
def is_onscreen(thing):
    # Apologies for this abomination of a line
    if thing.rect.centerx <= player.rect.centerx + constants.SCREEN_WIDTH and thing.rect.centerx >= player.rect.centerx - constants.SCREEN_WIDTH and thing.rect.centery <= player.rect.centery + constants.SCREEN_HEIGHT and thing.rect.centery >= player.rect.centery - constants.SCREEN_HEIGHT:
        return True

    return False

def changelevel(level_file):
    globals.bg_sprites.empty()
    globals.enemy_sprites.empty()
    globals.visible_sprites.empty()
    globals.active_sprites.empty()
    newlevel = levels.Customlevel(level_file)
    globals.active_sprites.add(newlevel.enemy_list)
    return newlevel

def initplayer():
    p = player.Player(globals.current_level.player_start[0],globals.current_level.player_start[1])
    return p

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), flags)

# Set the level to load
globals.current_level = changelevel("level01.json")

# Initialize the player class and pass the current level to it, for collision detection
p1 = initplayer()

hud = hud.Hud(p1)

globals.active_sprites.add(globals.current_level.enemy_list)

for enemy in globals.current_level.enemy_list:
    enemy.level = globals.current_level

# Initialize the camera class
cam = cam.Cam()

clock = pygame.time.Clock()

inp = input.InputHandler()
inp.player = p1

# Main loop
while globals.running:

    # Set the game to run at 60 FPS
    clock.tick(constants.FRAMERATE)

    inp.CheckInput()

    # Draw the background of the current level
    screen.blit(globals.current_level.background, (0,0))

    # Draw the background elements of the level, before any others
    for thing in globals.bg_sprites:
#        if is_onscreen(thing):
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    # Draw visible sprites, in relation to the camera's position.
    for thing in globals.visible_sprites:
#        if is_onscreen(thing):
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    screen.blit(hud.text, (hud.rect.x,hud.rect.y))
    hud.update()

    # Update the active sprites, unless the game is paused
    if not globals.paused:
        globals.player_sprites.update()
        globals.active_sprites.update()

    # If the player gets a certain amount of distance away from the center of the screen, the camera starts following them
    if p1.rect.right + cam.get_screen_center_x() > 5:
        cam.set_pos_x(p1.rect.right - constants.SCREEN_WIDTH * .5 - 5)
    
    if p1.rect.left + cam.get_screen_center_x() < -40:
        cam.set_pos_x(p1.rect.left - constants.SCREEN_WIDTH * .5 - -40)

    if p1.rect.bottom + cam.get_screen_center_y() > 15:
        cam.set_pos_y(p1.rect.bottom - constants.SCREEN_HEIGHT * .5 - 15)
        
    if p1.rect.top + cam.get_screen_center_y() < -30:
        cam.set_pos_y(p1.rect.top - constants.SCREEN_HEIGHT * .5 - -30)

    # Update the image
    pygame.display.flip()
