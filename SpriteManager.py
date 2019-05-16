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
    
class SpriteMap:
    def __init__(self, image):
        """Image is expected to be a pygame.image"""
        self.width = image.get_width()
        self.height = image.get_height()
        self.glTexture = glGenTextures(1)
        self.load_image(image)

    def __del__(self):
        # Delete image from gpu memory
        glDeleteTextures(self.glTexture)
    
    def load_image(self, image):
        """Replaces the image in the SpriteMap. image is expected to be a pygame.image."""
        self.width = image.get_width()
        self.height = image.get_height()
        image_data = pygame.image.tostring(image, "RGBA", True)
        self.bind()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        self.unbind()

    def bind(self):
        """Bind the texture to the active OpenGL texture unit."""
        glBindTexture(GL_TEXTURE_2D, self.glTexture)

    def unbind(self):
        """Unbind the active OpenGL texture unit."""
        glBindTexture(GL_TEXTURE_2D, 0)

    
class SpriteManager:
    """Creates and stores sprites, organized by spritemap for efficient rendering."""

    def __init__(self):
        self.sprites = {} # Dictionary of lists of Sprites indexed by SpriteMap

    def create_sprite(self):
        """Returns a new Sprite object managed by this SpriteManager."""
        pass

    def remove_sprite(self, sprite):
        """Removes a Sprite object from this SpriteManager."""
        # perhaps set sprite.manager to None to mark it as dead?
        pass

    def _spritemap_changed(self, sprite, old_spritemap):
        pass


class SpriteRenderer:
    """Renders the sprites in a SpriteManager"""
    def __init__(self, sprite_manager):
        self.sprite_manager = sprite_manager

    def render(self):
        pass
