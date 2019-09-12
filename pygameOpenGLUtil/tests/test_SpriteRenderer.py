import pygame
import pytest
from OpenGL.GL import *
from pygameOpenGLUtil import *
from pathlib import Path
from OpenGLTestUtils import *


def load_image(filename):
    filepath = str(Path(__file__).parent/"images"/filename)
    return pygame.image.load(filepath)


color_grid_image_path = str(Path(__file__).parent/"images/colorGrid.png")
inverted_color_grid_image_path = str(
    Path(__file__).parent/"images/colorGridInverted.png")
test_image_path = str(Path(__file__).parent/"images/test.png")


def test_render_one_sprite():
    expected_image = pygame.image.load(color_grid_image_path)
    openGLTestSetup(1024, 1024)
    
    # reset shader program id to none since the OpenGL context changed
    SpriteRenderer._shader_program = None

    spritemap = Texture(expected_image)
    sprite_manager = SpriteManager()
    sprite = Sprite(spritemap)
    sprite.width = 1024
    sprite.height = 1024
    sprite_manager.add_sprite(sprite)
    sprite_renderer = SpriteRenderer(sprite_manager)
    sprite_renderer.render()
    assert(is_rendered_image(expected_image))


def test_render_two_adjacent_sprites_from_same_spritemap():
    expected_image = load_image(
        "test_render_two_adjacent_sprites_from_same_spritemap.png")
    openGLTestSetup(256, 128)

    # reset shader program id to none since the OpenGL context changed
    SpriteRenderer._shader_program = None
    
    color_grid_image = pygame.image.load(color_grid_image_path)
    spritemap = Texture(color_grid_image)
    sprite_manager = SpriteManager()
    sprite_a = Sprite(spritemap)
    sprite_a.width = 128
    sprite_a.height = 128
    sprite_manager.add_sprite(sprite_a)
    sprite_b = Sprite(spritemap)
    sprite_b.width = 128
    sprite_b.height = 128
    sprite_b.x = 128
    sprite_b.spritemap_x = 256
    sprite_b.spritemap_y = 128
    sprite_manager.add_sprite(sprite_b)
    print(sprite_manager.sprites)
    sprite_renderer = SpriteRenderer(sprite_manager)
    sprite_renderer.render()
    assert(is_rendered_image(expected_image))


def test_render_two_adjacent_sprites_from_different_spritemaps():
    expected_image = load_image(
        "test_render_two_adjacent_sprites_from_different_spritemaps.png")
    openGLTestSetup(256, 128)

    # reset shader program id to none since the OpenGL context changed
    SpriteRenderer._shader_program = None

    sprite_manager = SpriteManager()
    image0 = pygame.image.load(color_grid_image_path)
    image1 = pygame.image.load(inverted_color_grid_image_path)
    texture0 = Texture(image0)
    texture1 = Texture(image1)
    sprite0 = Sprite(texture0)
    sprite0.width = 128
    sprite0.height = 128
    sprite0.spritemap_x = 768
    sprite0.spritemap_y = 256
    sprite1 = Sprite(texture1)
    sprite1.width = 128
    sprite1.height = 128
    sprite1.spritemap_x = 640
    sprite1.spritemap_y = 768
    sprite1.x = 128
    sprite_manager.add_sprite(sprite0)
    sprite_manager.add_sprite(sprite1)
    sprite_renderer = SpriteRenderer(sprite_manager)
    sprite_renderer.render()
    assert(is_rendered_image(expected_image))


# Crashes on certain OpenGL implementations, Josh will fix soon
# def test_render_overlapping_sprites_with_alpha():
#     expected_image = load_image("test_render_overlapping_sprites_with_alpha.png")
#     openGLTestSetup(1024, 1024)
#     sprite_manager = SpriteManager()
#     image0 = pygame.image.load(color_grid_image_path)
#     image1 = pygame.image.load(test_image_path)
#     texture0 = Texture(image0)
#     texture1 = Texture(image1)
#     sprite0 = Sprite(texture0)
#     sprite0.width = 1024
#     sprite0.height = 1024
#     sprite1 = Sprite(texture1)
#     sprite1.width = 512
#     sprite1.height = 319
#     sprite1.z = -0.1
#     sprite_manager.add_sprite(sprite0)
#     sprite_manager.add_sprite(sprite1)
#     sprite_renderer = SpriteRenderer(sprite_manager)
#     sprite_renderer.render()
#     save_image("test_results/test_render_overlapping_sprites_with_alpha.png")
#     assert(is_rendered_image(expected_image))
