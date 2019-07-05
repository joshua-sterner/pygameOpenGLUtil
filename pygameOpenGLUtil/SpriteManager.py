import pygame
from OpenGL.GL import *


class SpriteManager:
    """Creates and stores sprites, organized by spritemap for efficient
    rendering."""

    def __init__(self):
        # Dictionary of lists of Sprites indexed by SpriteMap
        self.sprites = {}

    def add_sprite(self, sprite):
        """adds a Sprite object to this SpriteManager."""
        if(self._sprite_in_dict(sprite)):
            self.sprites[sprite.spritemap].add(sprite)
        else:
            self.sprites[sprite.spritemap] = set([sprite])

    def remove_sprite(self, sprite):
        """Removes a Sprite object from this SpriteManager."""
        sprite_map = sprite.spritemap #Stores the Key that should be in the dict.
        #Check if spritemap in dictionary
        if(sprite_map in self.sprites):
            #Check if sprite is in the set.
            try:
                self.sprites[sprite_map].remove(sprite)
            except KeyError:
                raise KeyError("Sprite not in the SpriteManager")
            #Set Sprite's Sprite Manager to None.
            sprite.manager = None
            #Check if this is the last sprite in the set. If so delete the key.
            if(len(self.sprites[sprite_map]) == 0):
                del self.sprites[sprite_map]
        else:
            raise KeyError("SpriteMap not in Sprite Manager")


    def _spritemap_changed(self, sprite, old_spritemap):
        pass

    #Checks if sprite map in dictionary.
    def _sprite_map_in_dict(self, sprite):
        return sprite.spritemap in self.sprites
    
    #Checks if sprite is in the set represented by it's spritemap
    def _sprite_in_dict(self, sprite):
        if(sprite.spritemap in self.sprites):
            return sprite in self.sprites[sprite.spritemap]
        else:
            return False
