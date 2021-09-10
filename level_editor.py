import pygame
import csv
import globals
import constants
import levels
import platforms
import cam
import player

from pygame.locals import (
    K_ESCAPE,
    K_PAUSE,
    K_w,
    K_a,
    K_s,
    K_d,
    K_DOWN,
    K_UP,
    KEYDOWN,
    QUIT,
)

""" A rudimentary level editor """

class CursorPosition(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((1,1))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        #globals.active_sprites.add(self)

    def setpos(self, x, y):
        self.rect.x = x
        self.rect.y = y


# Initialize pygame
pygame.init()

#

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.EDITOR_SCREEN_WIDTH, constants.EDITOR_SCREEN_HEIGHT), flags)

# Set the level to load
current_level = levels.BlankLevel()

player = player.Player(current_level.player_start[0],current_level.player_start[1])


globals.active_sprites.add(current_level.wall_list) 
globals.active_sprites.add(current_level.platform_list)
globals.active_sprites.add(player)
globals.active_sprites.add(current_level.enemy_list)

# Variable to keep the main loop running
running = True

clock = pygame.time.Clock()

cam = cam.Cam()

blocklist = [platforms.Tan_Tile_01,
            platforms.Ground_Tile_01,
            platforms.Ground_Tile_02,
            platforms.Ground_Tile_03,
            platforms.Ground_Tile_04,
            platforms.Ground_Tile_05,
            platforms.Ground_Tile_06,]

pos = (0,0)

selected_block = 1
cursorpos = CursorPosition()

wall_list = pygame.sprite.Group()


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
            if event.key == K_UP:
                selected_block += 1
                if selected_block >= len(blocklist):
                    selected_block = 0
                print(str(selected_block))
            if event.key == K_DOWN:
                selected_block -= 1
                if selected_block < 0:
                    selected_block = len(blocklist) - 1                    
                print(str(selected_block))

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

    blockpreview = blocklist[selected_block]((pos[0] - cam.x), (pos[1] - cam.y))

    for thing in globals.active_sprites:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))
        
    screen.blit(blockpreview.surf,(blockpreview.rect.x + cam.x, blockpreview.rect.y + cam.y))
    pos = pygame.mouse.get_pos()
    cursorpos.rect.x = pos[0] - cam.x
    cursorpos.rect.y = pos[1] - cam.y

    

    if pygame.mouse.get_pressed()[0] == 1:
        #print(str((pos[0] - cam.x) // 8 * 8) + " " + str((pos[1] - cam.y) // 8 * 8))
        tile = blocklist[selected_block]((pos[0] - cam.x) // 8 * 8, (pos[1] - cam.y) // 8 * 8)
        hits = pygame.sprite.spritecollide(tile, globals.active_sprites, False)
        if len(hits) <= 0:
            globals.active_sprites.add(tile)
            print("Block placed at " + str((pos[0] - cam.x) // 8 * 8) + " " + str((pos[1] - cam.y) // 8 * 8))
            wall_list.add(tile)
        else:
            pygame.sprite.Sprite.kill(tile)


    if pygame.mouse.get_pressed()[2] == 1:
        #print(str((pos[0] - cam.x) // 8 * 8) + " " + str((pos[1] - cam.y) // 8 * 8))
        hits = pygame.sprite.spritecollide(cursorpos, globals.active_sprites, False)
        for hit in hits:
            pygame.sprite.Sprite.kill(hit)
    


    pygame.display.update()

