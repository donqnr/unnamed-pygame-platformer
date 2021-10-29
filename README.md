# unnamed-pygame-platformer
A platformer developed with pygame, along with a level editor

Very work-in-progress, even moreso with the level editor

Requires:

    Python 3: https://www.python.org/
    Pygame: https://www.pygame.org

Run __init__.py to start the game
level_editor.py for the level editor

Game Controls:

    Arrow keys: Move
    Spacebar: Jump
    Left Control: Shoot


Level editor controls:

    WASD: Move
    Up and Down arrow keys: Changes the selected block/enemy
    Left Mouse Button: Places a block/enemy
    Right Mouse Button: Removes a block/enemy

    F1: Selects a wall (Blocks player)
    F2: Selects a platform (Player can go through and stand on top of)
    F3: Selects a background object (Player goes through and displays behind the player)
    F4: Selects an enemy (Tries to kill the player)

    F6: Saves the level into (Currently only saves into saved_level.json, be sure to backup/rename the file after saving to prevent it from being overwritten)
    F7: Loads a level (Again, currently only loads saved_level.json, if there is one)
