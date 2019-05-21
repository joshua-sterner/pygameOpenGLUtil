import pygame
from OpenGL.GL import *
from pygameOpenGLUtil import *


class SpriteManagerTest(OpenGLTestCase):
    def test_add_sprite(self):
        test_sprite_map = SpriteManager()
        test_sprite_one = Sprite(test_sprite_map)
        test_sprite_one = Sprite(test_sprite_map)


if __name__ == "__main__":
    unittest.main()