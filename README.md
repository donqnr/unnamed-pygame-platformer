# unnamed-pygame-platformer

A platformer developed with pygame, along with a level editor

Very work-in-progress, even moreso with the level editor

Requires:

Python 3: https://www.python.org/

Pygame: https://www.pygame.org

Run \_\_init\_\_.py to start the game  
level_editor.py for the level editor

Game Controls:

    Arrow keys: Move
    Spacebar: Jump
    Left Control: Shoot
    Number keys: Select weapon
        1: Plasma Rifle
        2: Machine Gun
        3: Rocket Launcher
        4: Grenade Launcher
    Pause: Pause the game
    F12: Hide/Show HUD


Level editor controls:

    WASD: Move
    Up and Down arrow keys: Changes the selected block/enemy
    Left Mouse Button: Places a block/enemy
    Right Mouse Button: Removes a block/enemy

    1: Selects a wall (Blocks player)
    2: Selects a platform (Player can go through and stand on top of)
    3: Selects a background object (Player goes through and displays behind the player)
    4: Selects an enemy (Tries to kill the player)
    5: Selects a pickup (Health, Ammo)

    F6: Saves the level into (Currently only saves into saved_level.json, be sure to backup/rename the file after saving to prevent it from being overwritten)
    F7: Loads a level (Again, currently only loads saved_level.json, if there is one)
   
![screenshot](https://i.imgur.com/V6c3JNa.png)
![screenshot](https://i.imgur.com/iopwe1t.png)
![screenshot](https://i.imgur.com/ge2TcYV.png)
