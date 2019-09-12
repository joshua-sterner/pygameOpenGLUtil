import pygame
from OpenGL.GL import *


class Sprite:
    def __init__(self, sprite_map, spritemap_pos=(0,0), size=(0,0)):
        self.width = size[0]
        self.height = size[1]
        self.x = 0
        self.y = 0
        self.z = 0
        self._spritemap = sprite_map
        self.spritemap_x = spritemap_pos[0]
        self.spritemap_y = spritemap_pos[1]
        self._manager = None
    
    @property
    def spritemap(self):
        return self._spritemap

    @spritemap.setter
    def spritemap(self, spritemap):
        # Remember old spritemap
        old_spritemap = self._spritemap

        # Change the spritemap
        self._spritemap = spritemap

        # Notify manager of change from old spritemap
        self._manager._spritemap_changed(self, old_spritemap)
