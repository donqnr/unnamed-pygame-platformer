import pygame
import levels
import player
import constants
import globals

from pygame.locals import (
    K_ESCAPE,
    K_PAUSE,
    KEYDOWN,
    QUIT,
)

class Cam():

    # Camera component, follows the player when they move around the level
    def __init__(self):
        super(Cam, self).__init__()
        self.x = 0
        self.y = 0
    
    # Get center of the screen in x axis
    def get_screen_center_x(self):
        return cam.x - constants.SCREEN_WIDTH * .5
    # Get center of the screen in y axis
    def get_screen_center_y(self):
        return cam.y - constants.SCREEN_HEIGHT * .5
    # Set camera's position in x axis
    def set_pos_x(self, set_x):
        cam.x = -set_x
    # Set camera's position in y axis
    def set_pos_y(self, set_y):
        cam.y = -set_y


# Initialize pygame
pygame.init()

#

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), flags)

# Set the level to load
current_level = levels.TestLevel()


# Initialize the player class and pass the current level to it, for collision detection
player = player.Player(0,50)
player.level = current_level

globals.active_sprites.add(current_level.wall_list) 
globals.active_sprites.add(current_level.platform_list)
globals.active_sprites.add(player)
globals.active_sprites.add(current_level.enemy_list)

for enemy in current_level.enemy_list:
    enemy.level = current_level

# Initialize the camera class
cam = Cam()

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
            if event.key == pygame.K_SPACE and not globals.paused:
                player.jump()
            # If the key was left ctrl, try to shoot
            if event.key == pygame.K_LCTRL and not globals.paused:
                player.shoot()
            # If the key was pause, pause the game
            if event.key == pygame.K_PAUSE:
                if globals.paused:
                    globals.paused = False
                else:
                    globals.paused = True
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Draw the background of the current level
    screen.blit(current_level.background, (0,0))

    # Draw the walls and the platforms from the current level, which are drawn in relation to the position of the camera
    """ for wall in current_level.wall_list:
        screen.blit(wall.surf,(wall.rect.x + cam.x, wall.rect.y + cam.y))
    
    for plat in current_level.platform_list:
        screen.blit(plat.surf,(plat.rect.x + cam.x, plat.rect.y + cam.y)) """

    # Draw the player character
    #screen.blit(player.image, (player.rect.x + cam.x, player.rect.y + cam.y))

    # Draw active sprites, in relation to the camera's position
    for thing in globals.active_sprites:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    # Update the active sprites, unless the game is paused
    if not globals.paused:
        globals.active_sprites.update()

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
    pygame.display.flip()
