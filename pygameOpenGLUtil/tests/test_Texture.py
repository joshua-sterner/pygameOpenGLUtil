#!/usr/bin/env python

import pygame
import pytest
from OpenGL.GL import *
from pygameOpenGLUtil import *
from pathlib import Path
from OpenGLTestUtils import *

image_path = str(Path(__file__).parent/"images/test.png")
image2_path = str(Path(__file__).parent/"images/test3.png")

@pytest.fixture(autouse=True)
def setup(request):
    openGLTestSetup(1, 1)

def make_texture():
    image = pygame.image.load(image_path)
    return Texture(image)

def test_texture_bind_binds_a_texture():
    texture = make_texture()

    texture.bind()

    boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
    assert(boundTexture != 0)

def test_texture_glTexture_non_zero():
    texture = make_texture()

    assert(texture.glTexture > 0)

def test_texture_glTexture_is_valid_texture():
    texture = make_texture()

    assert(glIsTexture(texture.glTexture))

def test_texture_constructor_unbinds_texture():
    texture = make_texture()

    boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
    assert(boundTexture == 0)

def test_unbind_unbinds_texture():
    texture = make_texture()

    texture.bind()
    texture.unbind()

    boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
    assert(boundTexture == 0)

def test_init_loads_image_into_texture():
    image = pygame.image.load(image_path)
    texture = Texture(image)
    image_bytes = pygame.image.tostring(image, "RGBA", True)
    texture.bind()
    stored_bytes = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA,
                                 GL_UNSIGNED_BYTE)
    texture.unbind()
    assert(image_bytes == stored_bytes)

def test_del_unloads_texture_from_gpu_memory():
    texture = make_texture()
    glTexture = texture.glTexture

    del texture

    assert(not glIsTexture(glTexture))

def test_init_sets_correct_width():
    image = pygame.image.load(image_path)
    texture = Texture(image)
    assert(texture.width == 512)

def test_init_sets_correct_height():
    image = pygame.image.load(image_path)
    texture = Texture(image)
    assert(texture.height == 319)

def load_image_test_setup():
    image = pygame.image.load(image_path)
    texture = Texture(image)
    image2 = pygame.image.load(image2_path)
    texture.load_image(image2)
    return texture, image2

def test_load_image_sets_correct_width():
    texture, image2 = load_image_test_setup()
    assert(texture.width == 128)

def test_load_image_sets_correct_height():
    texture, image2 = load_image_test_setup()
    assert(texture.height == 256)

def test_load_image_loads_image_into_texture():
    texture, image2 = load_image_test_setup()
    image2_bytes = pygame.image.tostring(image2, "RGBA", True)
    texture.bind()
    stored_bytes = glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA,
                                 GL_UNSIGNED_BYTE)
    texture.unbind()
    assert(image2_bytes == stored_bytes)

def test_load_image_unbinds_texture():
    texture, image2 = load_image_test_setup()
    boundTexture = glGetIntegerv(GL_TEXTURE_BINDING_2D)
    assert(boundTexture == 0)

