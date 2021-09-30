import pygame

active_sprites = pygame.sprite.Group() # Sprites that are updated each frame (Player, enemies)
visible_sprites = pygame.sprite.Group() # Group to handle the visibility of a sprite
enemy_sprites = pygame.sprite.Group() # Group for handling hit detection of an enemy
player_sprites = pygame.sprite.Group() # Group for handling hit of a player
bg_sprites = pygame.sprite.Group() # Group for background blocks, to be blitted before other elements of the level

paused = False # Boolean to handle pausing