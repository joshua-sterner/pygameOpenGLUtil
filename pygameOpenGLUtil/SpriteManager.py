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
        
        #Check if the spritemap is in the dictionary.
        if(sprite_map in self.sprites):
            #Check if sprite is in the set.
            if(sprite in self.sprites[sprite_map]):
                #Remove sprite
                self.sprites[sprite_map].discard(sprite)
                #Set sprite.manager to None so the Sprite manager updates
                sprite.manager = None
                #Check if that was the last sprite in the set.
                if(len(self.sprites[sprite_map]) == 0):
                    del self.sprites[sprite_map]

                

    def _spritemap_changed(self, sprite, old_spritemap):
        pass

    def _sprite_in_dict(self, sprite):
        return sprite.spritemap in self.sprites
