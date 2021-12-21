from pygame import Surface, sprite
from scripts import globals, spritesheet
class LevelEnd(sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(LevelEnd, self).__init__()
        sprite.Sprite.__init__(self)
        self.sheet = spritesheet.SpriteSheet("assets/sprites/exitblock.png", 1)
        self.surf = self.sheet.get_image(31,10,14,8)
        self.surf = Surface((16,16))
        self.rect = self.surf.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        hits = sprite.spritecollide(self, globals.player_sprites, False)
        for hit in hits:
            if globals.current_level.nextlevel is not None:
                globals.changelevel(globals.current_level.nextlevel)