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
        if(sprite.spritemap in self.sprites):
            self.sprites[sprite.spritemap].add(sprite)
        else:
            self.sprites[sprite.spritemap] = set([sprite])

        # self.sprites[sprite.spritemap] = set([sprite])

    def remove_sprite(self, sprite):
        """Removes a Sprite object from this SpriteManager."""
        # should set sprite.manager to None
        pass

    def _spritemap_changed(self, sprite, old_spritemap):
        pass
