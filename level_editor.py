import pygame
import json

import vars
import constants
import levels
import cam
import player
import things

from pygame.locals import (
    K_ESCAPE,
    K_w,
    K_a,
    K_s,
    K_d,
    K_DOWN,
    K_UP,
    KEYDOWN,
    QUIT,
    K_F1,
    K_F2,
    K_F3,
    K_F4,
    K_F5,
    K_F6,
    K_F7,
)

""" A very rudimentary level editor """

# Set the level to load
current_level = levels.BlankLevel()

# A sprite for the position of the cursor, used to check if there's something on the spot where the cursor is pointed
class CursorPosition(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((1,1))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        #vars.active_sprites.add(self)

    def setpos(self, x, y):
        self.rect.x = x
        self.rect.y = y

# Function for saving the level to a json file
def save_level(list):
    with open("saved_level.json", 'w') as file:
        data = [(thing.name, thing.rect.topleft, thing.type)
                for thing in list]
        json.dump(data, file)

# Function to load an existing level
def load_level():
    with open("saved_level.json", 'r') as file:
        data = json.load(file)
        vars.active_sprites.empty()
        current_level.wall_list.empty()
        thing_list.empty()
        for block, pos, thingtype in data:
            thing = getattr(things, block)(pos[0],pos[1])
            thing.type = thingtype
            if thing.type == "bg":
                current_level.bg_list.add(thing)
                vars.active_sprites.add(thing)
            elif thing.type == "wall":
                current_level.wall_list.add(thing)
                vars.active_sprites.add(thing)
            elif thing.type == "platform":
                current_level.platform_list.add(thing)
                vars.active_sprites.add(thing)
            elif thing.type == "enemy":
                current_level.enemy_list.add(thing)
                vars.active_sprites.add(thing)
            thing_list.add(thing)
        
def add_to_list(tile):
    if tile.type == "bg":
        current_level.bg_list.add(tile)
    elif tile.type == "wall":
        current_level.wall_list.add(tile)
    elif tile.type == "platform":
        current_level.platform_list.add(tile)
    elif tile.type == "enemy":
        current_level.enemy_list.add(tile)
    vars.active_sprites.add(tile)

# Initialize pygame
pygame.init()

#

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
flags = pygame.SCALED | pygame.RESIZABLE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((constants.EDITOR_SCREEN_WIDTH, constants.EDITOR_SCREEN_HEIGHT), flags)


# Place the player class to indicate where the player start's going to be
player = player.Player(current_level.player_start[0],current_level.player_start[1])

# Add the level sprites and the player to the active sprites list
vars.active_sprites.add(player)

# Variable to keep the main loop running
running = True

clock = pygame.time.Clock()

# Set up the camera class
cam = cam.Cam()

# List of all the tiles that can be placed
blocklist = [things.Tan_Tile_01,
            things.Tan_Tile_01_B,
            things.Tan_Tile_02,
            things.Tan_Tile_02_B,
            things.Tan_Tile_03,
            things.Tan_Tile_03_B,
            things.Tan_Tile_04,
            things.Tan_Tile_04_B,
            things.Tan_Pipe_01,
            things.Tan_Pipe_02,
            things.Tan_Pipe_03,
            things.Tan_Pipe_04,
            things.Tan_Pipe_05,
            things.Tan_Pipe_06,
            things.Tan_Pipe_07,
            things.Tan_Panel_TL,
            things.Tan_Panel_T,
            things.Tan_Panel_TR,
            things.Tan_Panel_L,
            things.Tan_Panel_M,
            things.Tan_Panel_R,
            things.Tan_Panel_BL,
            things.Tan_Panel_B,
            things.Tan_Panel_BR,
            things.Pipe_Y_01,
            things.Pipe_Y_01_B,
            things.Ground_Tile_01,
            things.Ground_Tile_02,
            things.Ground_Tile_03,
            things.Ground_Tile_04,
            things.Ground_Tile_05,
            things.Ground_Tile_06,]

enemylist = [things.Enemy_01,]

# Position of the cursor on the screen
pos = (0,0)

# Which tile from the list is selected and gets placed
selected_block = 0
# Which enemy from the list is selected and gets placed
selected_enemy = 0

selected_thing_list = blocklist
selected_thing = selected_block

blockpreview = selected_thing_list[selected_thing]((pos[0] - cam.x), (pos[1] - cam.y))
blockpreview.surf.set_alpha(150)

# List of layers to place things in
thing_types = ['wall', 'platform', 'bg', 'fg', 'enemy']
# Variable for determining which layer to place a tile (background, foreground, walls) or if it's an enemy or a pickup
selected_thing_type = "wall"
# Initialize the sprite which follows the cursor
cursorpos = CursorPosition()

# List of placed things that gets passed onto the save function
thing_list = pygame.sprite.Group()

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
            # Go up the list of placeable blocks
            if event.key == K_UP:
                selected_thing += 1
                if selected_thing >= len(selected_thing_list):
                    selected_thing = 0
            # Go down the list of placeable blocks
            if event.key == K_DOWN:
                selected_thing -= 1
                if selected_thing < 0:
                    selected_thing = len(selected_thing_list) - 1
            # Set the tile to be placed as a wall
            if event.key == K_F1:
                selected_thing_type = "wall"
                selected_thing_list = blocklist
                selected_thing = selected_block
                print("Wall")
            # Set the tile to be placed as a platform
            if event.key == K_F2:
                selected_thing_type = "platform"
                selected_thing_list = blocklist
                selected_thing = selected_block
                print("Platform")
            # Set the tile to be placed in the background
            if event.key == K_F3:
                selected_thing_type = "bg"
                selected_thing_list = blocklist
                selected_thing = selected_block
                print("Background")
            # Set the tile to be placed to be an enemy
            if event.key == K_F4:
                selected_thing_type = "enemy"
                selected_thing_list = enemylist
                selected_thing = selected_enemy
                print("Enemy")
            # Save the current level into a file                    
            if event.key == K_F6:
                save_level(thing_list)
            # Load a level from a file
            if event.key == K_F7:
                load_level()

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()

    # Move the camera around the level
    if pressed_keys[K_a]:
        cam.x += 2
    if pressed_keys[K_d]:
        cam.x -= 2
    if pressed_keys[K_w]:
        cam.y += 2
    if pressed_keys[K_s]:
        cam.y -= 2
        
    # Blit the level background
    screen.blit(pygame.transform.scale(current_level.background, (constants.EDITOR_SCREEN_WIDTH,constants.EDITOR_SCREEN_HEIGHT)), (0,0))

    # A preview for the currently selected block
    blockpreview = selected_thing_list[selected_thing]((pos[0] - cam.x), (pos[1] - cam.y))

    # Blit all the active sprites
    """ for thing in vars.active_sprites:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y)) """


    for thing in current_level.bg_list:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    for thing in current_level.wall_list:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    for thing in current_level.platform_list:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))

    for thing in current_level.enemy_list:
        screen.blit(thing.surf,(thing.rect.x + cam.x, thing.rect.y + cam.y))
        
    screen.blit(player.surf,(player.rect.x + cam.x, player.rect.y + cam.y))
    # Blit the preview for the selected block on the cursor
    screen.blit(blockpreview.surf,(blockpreview.rect.x + cam.x, blockpreview.rect.y + cam.y))

    # Set pos as the mouse cursor position
    pos = pygame.mouse.get_pos()

    # Move the cursorpos sprite to where the mouse is pointing, take the camera position into account
    cursorpos.rect.x = pos[0] - cam.x
    cursorpos.rect.y = pos[1] - cam.y


    if pygame.mouse.get_pressed()[0] == 1:
        tile = selected_thing_list[selected_thing]((pos[0] - cam.x) // 8 * 8, (pos[1] - cam.y) // 8 * 8)
        if selected_thing_type == "wall" or "platform":
            hits = pygame.sprite.spritecollide(tile, current_level.wall_list, False)
            hits.extend(pygame.sprite.spritecollide(tile, current_level.platform_list, False))
        if selected_thing_type == "bg":
            hits = pygame.sprite.spritecollide(tile, current_level.bg_list, False)
        if selected_thing_type == "enemy":
            hits = pygame.sprite.spritecollide(tile, current_level.enemy_list, False) 
        if len(hits) == 0:
            vars.visible_sprites.add(tile)
            print(tile.name + " placed at " + str((pos[0] - cam.x) // 8 * 8) + " " + str((pos[1] - cam.y) // 8 * 8) + " as " + selected_thing_type)
            if tile.type == "wall":
                tile.type = selected_thing_type 
            add_to_list(tile)
            thing_list.add(tile)
        else:
            pygame.sprite.Sprite.kill(tile)


    if pygame.mouse.get_pressed()[2] == 1:
        hits = pygame.sprite.spritecollide(cursorpos, vars.active_sprites, False)
        for hit in hits:
            pygame.sprite.Sprite.kill(hit)
            print("Removed " + hit.type + " " + hit.name)
    


    pygame.display.update()

