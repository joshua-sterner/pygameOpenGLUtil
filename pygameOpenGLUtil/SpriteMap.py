import pygame
from OpenGL.GL import *


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
        """Replaces the image in the SpriteMap. image is expected to be a
        pygame.image."""
        self.width = image.get_width()
        self.height = image.get_height()
        image_data = pygame.image.tostring(image, "RGBA", True)
        self.bind()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        self.unbind()

    def bind(self):
        """Bind the texture to the active OpenGL texture unit."""
        glBindTexture(GL_TEXTURE_2D, self.glTexture)

    def unbind(self):
        """Unbind the active OpenGL texture unit."""
        glBindTexture(GL_TEXTURE_2D, 0)
