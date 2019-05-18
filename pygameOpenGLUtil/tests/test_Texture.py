#!/usr/bin/env python

import pygame
import unittest
from OpenGL.GL import *
from pygameOpenGLUtil import *
from pathlib import Path

image_path = str(Path(__file__).parent/"test.png")
image2_path = str(Path(__file__).parent/"test3.png")

class TextureTests(OpenGLTestCase):

    def make_texture(self):
        image = pygame.image.load(image_path)
        return Texture(image)

    def setUp(self):
        self.set_render_size(1, 1)

    def test_texture_bind_binds_a_texture(self):
        texture = self.make_texture()

        texture.bind()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertNotEqual(boundTexture, 0)

    def test_texture_glTexture_non_zero(self):
        texture = self.make_texture()

        self.assertTrue(texture.glTexture > 0)

    def test_texture_glTexture_is_valid_texture(self):
        texture = self.make_texture()

        self.assertTrue(glIsTexture(texture.glTexture))

    def test_texture_constructor_unbinds_texture(self):
        texture = self.make_texture()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)

    def test_unbind_unbinds_texture(self):
        texture = self.make_texture()

        texture.bind()
        texture.unbind()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)

    def test_init_loads_image_into_texture(self):
        image = pygame.image.load(image_path)
        texture = Texture(image)
        image_bytes = pygame.image.tostring(image, "RGBA", True)
        texture.bind()
        stored_bytes = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA,
                                     GL_UNSIGNED_BYTE)
        texture.unbind()
        self.assertEqual(image_bytes, stored_bytes)

    def test_del_unloads_texture_from_gpu_memory(self):
        texture = self.make_texture()
        glTexture = texture.glTexture

        del texture

        self.assertFalse(glIsTexture(glTexture))

    def test_init_sets_correct_width(self):
        image = pygame.image.load(image_path)
        texture = Texture(image)
        self.assertEqual(texture.width, 512)

    def test_init_sets_correct_height(self):
        image = pygame.image.load(image_path)
        texture = Texture(image)
        self.assertEqual(texture.height, 319)

    def load_image_test_setup(self):
        image = pygame.image.load(image_path)
        texture = Texture(image)
        image2 = pygame.image.load(image2_path)
        texture.load_image(image2)
        return texture, image2

    def test_load_image_sets_correct_width(self):
        texture, image2 = self.load_image_test_setup()
        self.assertEqual(texture.width, 128)

    def test_load_image_sets_correct_height(self):
        texture, image2 = self.load_image_test_setup()
        self.assertEqual(texture.height, 256)

    def test_load_image_loads_image_into_texture(self):
        texture, image2 = self.load_image_test_setup()
        image2_bytes = pygame.image.tostring(image2, "RGBA", True)
        texture.bind()
        stored_bytes = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA,
                                     GL_UNSIGNED_BYTE)
        texture.unbind()
        self.assertEqual(image2_bytes, stored_bytes)

    def test_load_image_unbinds_texture(self):
        texture, image2 = self.load_image_test_setup()
        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)


if __name__ == "__main__":
    unittest.main()
