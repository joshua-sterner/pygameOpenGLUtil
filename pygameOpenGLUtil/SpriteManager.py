import pygame
from OpenGL.GL import *


class SpriteManager:
    """Creates and stores sprites, organized by spritemap for efficient
    rendering."""

    def __init__(self):
        # Dictionary of lists of Sprites indexed by SpriteMap
        self.sprites = {}

    def create_sprite(self):
        """Returns a new Sprite object managed by this SpriteManager."""
        pass

    def remove_sprite(self, sprite):
        """Removes a Sprite object from this SpriteManager."""
        # perhaps set sprite.manager to None to mark it as dead?
        pass

    def _spritemap_changed(self, sprite, old_spritemap):
        pass
