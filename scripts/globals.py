from pygame import sprite
import levels

active_sprites = sprite.Group() # Sprites that are updated each frame (Player, enemies)
visible_sprites = sprite.Group() # Group to handle the visibility of a sprite
enemy_sprites = sprite.Group() # Group for handling hit detection of an enemy
player_sprites = sprite.Group() # Group for handling hit of a player
bg_sprites = sprite.Group() # Group for background blocks, to be blitted before other elements of the level

current_level = None # Currently loaded level

paused = False # Boolean to handle pausing
running = True # Variable to keep the main loop running

def changelevel(level_file):
    bg_sprites.empty()
    enemy_sprites.empty()
    visible_sprites.empty()
    active_sprites.empty()
    newlevel = levels.Customlevel(level_file)
    active_sprites.add(newlevel.enemy_list)
    return newlevel