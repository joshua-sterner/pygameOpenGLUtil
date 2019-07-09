import pygame
import pytest
from pygameOpenGLUtil import *
from pathlib import Path

@pytest.fixture
def baseline():
    # Create two "Fake sprite maps" with random images
    # This is not a sprite map
    image_path = str(Path(__file__).parent/"images/test.png")
    # This is not a sprite map
    image2_path = str(Path(__file__).parent/"images/test3.png")

    spritemap_1 = pygame.image.load(image_path)
    spritemap_2 = pygame.image.load(image2_path)

    # Create one sprite Managers
    test_sprite_manager = SpriteManager()

    # Create three sprites
    test_sprite_one = Sprite(spritemap_1)
    test_sprite_two = Sprite(spritemap_1)
    # This one has a different sprite map and image
    test_sprite_three = Sprite(spritemap_2)

    # Returns a list with references to the three objects created
    return [test_sprite_manager,  # Index 0 is the Sprite Manager
            [test_sprite_one, test_sprite_two, test_sprite_three]]  # Index 1 is the Sprites
