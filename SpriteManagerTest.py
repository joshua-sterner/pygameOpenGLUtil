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

    def test_spritemap_bind_binds_a_texture(self):
        self.set_render_size(1, 1)
        spritemap = make_spritemap()

        spritemap.bind()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertNotEqual(boundTexture, 0)
    
    def test_spritemap_glTexture_non_zero(self):
        self.set_render_size(1, 1)
        
        spritemap = make_spritemap()
        
        self.assertTrue(spritemap.glTexture > 0)

    def test_spritemap_glTexture_is_valid_texture(self):
        self.set_render_size(1, 1)

        spritemap = make_spritemap()
        
        self.assertTrue(glIsTexture(spritemap.glTexture))

    def test_spritemap_constructor_unbinds_texture(self):
        self.set_render_size(1, 1)

        spritemap = make_spritemap()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)

    def test_unbind_unbinds_texture(self):
        self.set_render_size(1, 1)
        spritemap = make_spritemap()

        spritemap.bind()
        spritemap.unbind()

        boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
        self.assertEqual(boundTexture, 0)


if __name__ == "__main__":
    
    unittest.main()
