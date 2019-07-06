import pygame
from OpenGL.GL import *


class SpriteManager:
    """Creates and stores sprites, organized by spritemap for efficient
    rendering."""

    def __init__(self):
        # Dictionary of lists of Sprites indexed by SpriteMap
        self._sprites = {}

    def add_sprite(self, sprite):
        """adds a Sprite object to this SpriteManager."""
        if(self.has_sprite(sprite)):
            self._sprites[sprite.spritemap].add(sprite)
        else:
            self._sprites[sprite.spritemap] = set([sprite])

    def remove_sprite(self, sprite):
        """Removes a Sprite object from this SpriteManager."""
        spritemap = sprite.spritemap #Stores the Key that should be in the dict.
        #Check if spritemap in dictionary
        if(spritemap in self._sprites):
            #Check if sprite is in the set.
            try:
                self._sprites[spritemap].remove(sprite)
            except KeyError:
                raise KeyError("Sprite not in the SpriteManager")
            #Set Sprite's Sprite Manager to None.
            sprite.manager = None
            #Check if this is the last sprite in the set. If so delete the key.
            if(len(self._sprites[spritemap]) == 0):
                del self._sprites[spritemap]
        else:
            raise KeyError("SpriteMap not in Sprite Manager")


    def _spritemap_changed(self, sprite, old_spritemap):
        try:
            self._sprites[old_spritemap].remove(sprite)
        except KeyError:
            raise KeyError("The sprite was not in the Sprite Manager or is" + 
            " under a different sprite map.")
        self.add_sprite(sprite)
        

    #Checks if sprite map in dictionary.
    def has_spritemap(self, sprite):
        return sprite.spritemap in self._sprites
    
    #Checks if sprite is in the set represented by it's spritemap
    def has_sprite(self, sprite):
        if(sprite.spritemap in self._sprites):
            return sprite in self._sprites[sprite.spritemap]
        else:
            return False
