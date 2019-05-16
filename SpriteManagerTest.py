#!/usr/bin/env python

import pygame
import unittest
from OpenGL.GL import *
import OpenGLTestCase
from SpriteManager import *

def make_spritemap():
    image = pygame.image.load("test.png")
    return SpriteMap(image)

class SpriteMapTests(OpenGLTestCase.OpenGLTestCase):
    def setUp(self):
        self.set_render_size(1, 1)

    def test_spritemap_bind_binds_a_texture(self):
        spritemap = make_spritemap()

        spritemap.bind()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertNotEqual(boundTexture, 0)
    
    def test_spritemap_glTexture_non_zero(self):
        spritemap = make_spritemap()
        
        self.assertTrue(spritemap.glTexture > 0)

    def test_spritemap_glTexture_is_valid_texture(self):
        spritemap = make_spritemap()
        
        self.assertTrue(glIsTexture(spritemap.glTexture))

    def test_spritemap_constructor_unbinds_texture(self):
        spritemap = make_spritemap()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)

    def test_unbind_unbinds_texture(self):
        spritemap = make_spritemap()

        spritemap.bind()
        spritemap.unbind()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)
    
    def test_init_loads_image_into_texture(self):
        image = pygame.image.load("test.png")
        spritemap = SpriteMap(image)
        image_bytes = pygame.image.tostring(image, "RGBA", True)
        spritemap.bind()
        stored_bytes = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_UNSIGNED_BYTE)
        spritemap.unbind()
        self.assertEqual(image_bytes, stored_bytes)

    def test_del_unloads_texture_from_gpu_memory(self):
        spritemap = make_spritemap()
        glTexture = spritemap.glTexture

        del spritemap

        self.assertFalse(glIsTexture(glTexture))
    
    def test_init_sets_correct_width(self):
        image = pygame.image.load("test.png")
        spritemap = SpriteMap(image)
        self.assertEqual(spritemap.width, 512)

    def test_init_sets_correct_height(self):
        image = pygame.image.load("test.png")
        spritemap = SpriteMap(image)
        self.assertEqual(spritemap.height, 319)

    def load_image_test_setup(self):
        image = pygame.image.load("test.png")
        spritemap = SpriteMap(image)
        image2 = pygame.image.load("test3.png")
        spritemap.load_image(image2)
        return spritemap, image2

    def test_load_image_sets_correct_width(self):
        spritemap, image2 = self.load_image_test_setup()
        self.assertEqual(spritemap.width, 128)

    def test_load_image_sets_correct_height(self):
        spritemap, image2 = self.load_image_test_setup()
        self.assertEqual(spritemap.height, 256)

    def test_load_image_loads_image_into_texture(self):
        spritemap, image2 = self.load_image_test_setup()
        image2_bytes = pygame.image.tostring(image2, "RGBA", True)
        spritemap.bind()
        stored_bytes = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_UNSIGNED_BYTE)
        spritemap.unbind()
        self.assertEqual(image2_bytes, stored_bytes)

    def test_load_image_unbinds_texture(self):
        spritemap, image2 = self.load_image_test_setup()
        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)

if __name__ == "__main__":
    unittest.main()
