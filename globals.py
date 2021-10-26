from pygame import sprite

active_sprites = sprite.Group() # Sprites that are updated each frame (Player, enemies)
visible_sprites = sprite.Group() # Group to handle the visibility of a sprite
enemy_sprites = sprite.Group() # Group for handling hit detection of an enemy
player_sprites = sprite.Group() # Group for handling hit of a player
bg_sprites = sprite.Group() # Group for background blocks, to be blitted before other elements of the level

current_level = None

paused = False # Boolean to handle pausing