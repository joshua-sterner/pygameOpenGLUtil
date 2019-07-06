#!/usr/bin/env python
import pygame
from OpenGL.GL import *
from pygameOpenGLUtil import *
from pathlib import Path

pygame.init()
pygame.display.set_mode((1280, 720), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
glViewport(0, 0, 1280, 720)
sprite_manager = SpriteManager()
image0 = pygame.image.load("pygameOpenGLUtil/tests/test.png")
image1 = pygame.image.load("pygameOpenGLUtil/tests/colorGrid.png")
texture1 = Texture(image1)
sprite0 = Sprite(sprite_manager, texture1)
sprite0.width = 128
sprite0.height = 128
sprite1 = Sprite(sprite_manager, texture1)
sprite1.width = 128
sprite1.height = 128
sprite1.spritemap_x = 512
sprite1.x = 96
sprite1.y = 32
sprite1.z = 0.1
sprite_manager.add_sprite(sprite0)
sprite_manager.add_sprite(sprite1)
print(sprite_manager.has_sprite(sprite0))
sprite_renderer = SpriteRenderer(sprite_manager)

key_pressed = False
while not key_pressed:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            key_pressed = True
    sprite_renderer.render()
    pygame.display.flip()
