import pygame
import pytest
from OpenGL.GL import *
from pygameOpenGLUtil import *
from pathlib import Path


@pytest.fixture
def baseline():
    # Create two "Fake sprite maps" with random images
    # This is not a sprite map
    image_path = str(Path(__file__).parent/"test.png")
    # This is not a sprite map
    image2_path = str(Path(__file__).parent/"test3.png")

    spritemap_1 = pygame.image.load(image_path)
    spritemap_2 = pygame.image.load(image2_path)

    # Create one sprite Managers
    test_sprite_manager = SpriteManager()

    # Create three sprites
    test_sprite_one = Sprite(test_sprite_manager, spritemap_1)
    test_sprite_two = Sprite(test_sprite_manager, spritemap_1)
    # This one has a different sprite map and image
    test_sprite_three = Sprite(test_sprite_manager, spritemap_2)

    # Returns a list with references to the three objects created
    return [test_sprite_manager,  # Index 0 is the Sprite Manager
            [test_sprite_one, test_sprite_two, test_sprite_three]]  # Index 1 is the Sprites


def test_add_sprite(baseline):
    # Check if you can add a sprite
    baseline[0].add_sprite(baseline[1][0])
    assert (baseline[0].has_sprite(baseline[1][0])) == True

    # Check if you can add another sprite from the same sprite map
    baseline[0].add_sprite(baseline[1][1])
    assert (baseline[0].has_sprite(baseline[1][1])) == True

    # Check if you can add another sprite from a different sprite map
    baseline[0].add_sprite(baseline[1][2])
    assert (baseline[0].has_sprite(baseline[1][2])) == True


def test_remove_sprite(baseline):
    # Add a sprite
    baseline[0].add_sprite(baseline[1][0])
    # Remove Sprite
    baseline[0].remove_sprite(baseline[1][0])
    # Check if Sprite is still there
    assert (baseline[0].has_sprite(baseline[1][0])) == False
    # Check if Sprite Manger = None for the sprite removed.
    assert (baseline[1][0].manager) == None

    # After removing the only sprite with that sprite map check if spritemap is
    # still a key value in the dict.
    assert (baseline[0].has_spritemap(baseline[1][0])) == False

    # Try and remove something that doesn't exist. This should throw a key
    # error, if it does not pytest will fail.
    with pytest.raises(KeyError):
        baseline[0].remove_sprite(baseline[1][0])


def test_spritemap_changed(baseline):
	# Add Sprites
    baseline[0].add_sprite(baseline[1][0])

    old_spritemap = baseline[1][0].spritemap

    # Create a new sprite map.
    # This is not an actaul spritemap.
    image_path = str(Path(__file__).parent/"test3.png")
    spritemap_2 = pygame.image.load(image_path)

    # Change spritemap
    baseline[1][0].spritemap = spritemap_2

	#Test comment
	
