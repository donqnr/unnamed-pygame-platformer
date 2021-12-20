from pygame import Surface, sprite
import globals, spritesheet
from globals import current_level, changelevel

class LevelEnd(sprite.Sprite):
    def __init__(self):
        super(LevelEnd, self).__init__()
        sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/exitblock.png", 1)
        self.surf = self.sheet.get_image(31,10,14,8)
        self.surf = Surface((16,16))
        self.rect = self.surf.get_rect()

    def update(self):
        hits = sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            if current_level.nextlevel is not None:
                changelevel(current_level.nextlevel)