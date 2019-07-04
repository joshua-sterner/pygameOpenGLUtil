import pygame
import pytest
import unittest
from OpenGL.GL import *
from pygameOpenGLUtil import *
from pathlib import Path


@pytest.fixture
def baseline():
    # Create two "Fake sprite maps" with random images
    image_path = str(Path(__file__).parent/"test.png")
    image2_path = str(Path(__file__).parent/"test3.png")

    sprite_map_1 = pygame.image.load(image_path)
    sprite_map_2 = pygame.image.load(image2_path)

    # Create one sprite Managers
    test_sprite_manager = SpriteManager()

    # Create three sprites
    test_sprite_one = Sprite(test_sprite_manager, sprite_map_1)
    test_sprite_two = Sprite(test_sprite_manager, sprite_map_1)
    # This one has a different sprite map and image
    test_sprite_three = Sprite(test_sprite_manager, sprite_map_2)

    # Returns a list with references to the three objects created
    return [test_sprite_manager,  # Index 0 is the Sprite Manager
            [test_sprite_one, test_sprite_two, test_sprite_three]]  # Index 1 is the Sprites


def test_add_sprite(baseline):
    # Check if you can add a sprite
    baseline[0].add_sprite(baseline[1][0])
    # Check if you can add another sprite from the same sprite map
    baseline[0].add_sprite(baseline[1][1])

    # Check if you can add another sprite from a different sprite map
    baseline[0].add_sprite(baseline[1][2])


def test_remove_sprite(baseline):
    #Add a sprite
    baseline[0].add_sprite(baseline[1][0])
    # Try and remove it
    baseline[0].remove_sprite(baseline[1][0])
    # Check if Sprite Manger = None for the sprite removed. 
    assert (baseline[1][0].manager) == None

    #Try and remove something that doesn't exist. 
    baseline[0].remove_sprite(baseline[1][1])


if __name__ == "__main__":
    unittest.main()