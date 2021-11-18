import pygame
from scripts import constants

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), flags)

from scripts import globals, input, player, ui, cam, levels

# Function to check if a sprite is near or in the viewport
def is_onscreen(thing):
    # Apologies for this abomination of a line
    if thing.rect.centerx <= player.rect.centerx + constants.SCREEN_WIDTH and thing.rect.centerx >= player.rect.centerx - constants.SCREEN_WIDTH and thing.rect.centery <= player.rect.centery + constants.SCREEN_HEIGHT and thing.rect.centery >= player.rect.centery - constants.SCREEN_HEIGHT:
        return True

    return False


def initplayer():
    p = player.Player(globals.current_level.player_start[0],globals.current_level.player_start[1])
    return p

# Set the level to load
globals.current_level = levels.Level01()

# Initialize the player class and pass the current level to it, for collision detection
p1: player.Player = initplayer()

# Initialize the HUD
globals.hud.set_player(p1)

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

    # Set the game to run at the specified framerate
    clock.tick(constants.FRAMERATE)

    # If the player gets a certain amount of distance away from the center of the screen, the camera starts following them
    if p1.rect.right + cam.get_screen_center_x() > 5:
        cam.set_pos_x(p1.rect.right - constants.SCREEN_WIDTH * .5 - 5)
    
    if p1.rect.left + cam.get_screen_center_x() < -40:
        cam.set_pos_x(p1.rect.left - constants.SCREEN_WIDTH * .5 - -40)

    if p1.rect.bottom + cam.get_screen_center_y() > 15:
        cam.set_pos_y(p1.rect.bottom - constants.SCREEN_HEIGHT * .5 - 15)
        
    if p1.rect.top + cam.get_screen_center_y() < -30:
        cam.set_pos_y(p1.rect.top - constants.SCREEN_HEIGHT * .5 - -30)

    # Draw the background of the current level
    screen.blit(globals.current_level.background, (0,0))

    # Draw the background elements of the level, before any others
    for thing in globals.bg_sprites:
#        if is_onscreen(thing):
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    # Update the active sprites, unless the game is paused
    if not globals.paused:
        globals.player_sprites.update()
        globals.active_sprites.update()
        

    # Draw visible sprites, in relation to the camera's position.
    for thing in globals.visible_sprites:
#        if is_onscreen(thing):
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    if not globals.hide_hud:
        screen.blit(globals.hud.hp.text, (globals.hud.hp.rect.x,globals.hud.hp.rect.y))
        screen.blit(globals.hud.ammo.text, (globals.hud.ammo.rect.x,globals.hud.ammo.rect.y))
        screen.blit(globals.hud.wpn.text, (globals.hud.wpn.rect.x,globals.hud.wpn.rect.y))
        screen.blit(globals.hud.msg.text, (globals.hud.msg.rect.x,globals.hud.msg.rect.y))

    globals.hud.update()

    inp.CheckInput()

    # Update the image
    pygame.display.update()