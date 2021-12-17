from pygame import sprite
from scripts import levels, ui, player

active_sprites = sprite.Group() # Sprites that are updated each frame (Player, enemies)
visible_sprites = sprite.Group() # Group to handle the visibility of a sprite
enemy_sprites = sprite.Group() # Group for handling hit detection of an enemy
player_sprites = sprite.Group() # Group for handling hit of a player
bg_sprites = sprite.Group() # Group for background blocks, to be blitted before other elements of the level

current_level: levels.Level = None # Currently loaded level

hud = ui.Hud()

p1: player.Player = None

paused: bool = False # Boolean to handle pausing
running: bool = True # Boolean to keep the main loop running
hide_hud: bool = False # Boolean to set HUD's visibility

def changelevel(level_class: levels.Level):
    bg_sprites.empty()
    enemy_sprites.empty()
    visible_sprites.empty()
    active_sprites.empty()
    newlevel = level_class
    bg_sprites.add(newlevel.bg_list)
    enemy_sprites.add(newlevel.enemy_list)

    visible_sprites.add(newlevel.bg_list, newlevel.enemy_list, newlevel.wall_list, newlevel.platform_list, player_sprites)
    active_sprites.add(newlevel.enemy_list)
    p1.rect.topleft = (newlevel.player_start[0], newlevel.player_start[1])
    return newlevel