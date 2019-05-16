import pygame
from OpenGL.GL import *


class Sprite:
    def __init__(self, sprite_manager):
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.spritemap = None
        self.spritemap_x = 0
        self.spritemap_y = 0
        self.manager = sprite_manager

    @property
    def spritemap(self):
        return self.__spritemap

    @spritemap.setter
    def spritemap(self, spritemap):
        # Remember old spritemap
        old_spritemap = self.__spritemap

        # Change the spritemap
        self.__spritemap = spritemap

        # Notify manager of change from old spritemap
        self.manager._spritemap_changed(self, old_spritemap)
