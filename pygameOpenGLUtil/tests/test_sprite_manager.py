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
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]


    # Check if you can add a sprite
    sprite_manager.add_sprite(sprite_one)
    assert (sprite_manager.has_sprite(sprite_one)) == True

    # Check if you can add another sprite from the same sprite map
    sprite_manager.add_sprite(sprite_two)
    assert (sprite_manager.has_sprite(sprite_two)) == True

    # Check if you can add another sprite from a different sprite map
    sprite_manager.add_sprite(sprite_three)
    assert (sprite_manager.has_sprite(sprite_three)) == True


def test_remove_sprite(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]

    # Add a sprite
    sprite_manager.add_sprite(sprite_one)
    # Remove Sprite
    sprite_manager.remove_sprite(sprite_one)
    # Check if Sprite is still there
    assert (sprite_manager.has_sprite(sprite_one)) == False
    # Check if Sprite Manger = None for the sprite removed.
    assert (sprite_one.manager) == None

    # After removing the only sprite with that sprite map check if spritemap is
    # still a key value in the dict.
    assert (sprite_manager.has_spritemap(sprite_one)) == False

    # Try and remove something that doesn't exist. This should throw a key
    # error, if it does not pytest will fail.
    with pytest.raises(KeyError):
        sprite_manager.remove_sprite(sprite_one)


def test_spritemap_changed(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]

    # Add Sprites
    sprite_manager.add_sprite(sprite_one)

    old_spritemap = sprite_one.spritemap

    # Create a new sprite map.
    # This is not an actaul spritemap.
    image_path = str(Path(__file__).parent/"test3.png")
    new_spritemap = pygame.image.load(image_path)

    # Change spritemap
    sprite_one.spritemap = new_spritemap

    # Check Sprite's Key has changed in Sprite Manager
    assert (sprite_one in sprite_manager.sprites[old_spritemap]) == False

    # Check if Sprite's Key in Sprite Manager is new Sprite Map
    assert (sprite_one in 
            sprite_manager.sprites[new_spritemap]) == True
    
