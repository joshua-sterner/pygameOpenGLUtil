import pygame
import pytest
from pygameOpenGLUtil import *
from pathlib import Path

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

def test_add_two_sprites(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]
    
    # Check if you can add another sprite from the same sprite map
    sprite_manager.add_sprite(sprite_one)
    sprite_manager.add_sprite(sprite_two)

    assert (sprite_manager.has_sprite(sprite_one)) == True
    assert (sprite_manager.has_sprite(sprite_two)) == True

def test_add_same_sprite_twice(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]

    sprite_manager.add_sprite(sprite_one)
    with pytest.raises(KeyError):
            sprite_manager.add_sprite(sprite_one)

def test_add_sprite_from_different_spritemap(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]

    # Check if you can add another sprite from a different sprite map
    sprite_manager.add_sprite(sprite_one)
    sprite_manager.add_sprite(sprite_two)
    sprite_manager.add_sprite(sprite_three)

    assert (sprite_manager.has_sprite(sprite_one))
    assert (sprite_manager.has_sprite(sprite_two)) == True
    assert (sprite_manager.has_sprite(sprite_three)) == True

def test_add_sprite_with_manager(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]

	#Create fake sprite manager
    fake_sprite_manager = SpriteManager()

	#Add the sprite to the  fake sprite manager
    fake_sprite_manager.add_sprite(sprite_one)
	
	#Try and add it to our original sprite manager
    with pytest.raises(AttributeError):
        sprite_manager.add_sprite(sprite_one)

def test_sprites_manager_pointer(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]

    sprite_manager.add_sprite(sprite_one)
    assert (sprite_one._manager == sprite_manager)

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

def test_removed_sprites_manager(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]

    # Add a sprite
    sprite_manager.add_sprite(sprite_one)
    # Remove Sprite
    sprite_manager.remove_sprite(sprite_one)

    # Check if Sprite Manger = None for the sprite removed.
    assert (sprite_one._manager) == None

def test_spritemap_removed_after_last_sprite(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]

    # Add a sprite
    sprite_manager.add_sprite(sprite_one)
    # Remove Sprite
    sprite_manager.remove_sprite(sprite_one)

    # After removing the only sprite with that sprite map check if spritemap is
    # still a key value in the dict.
    assert (sprite_manager.has_spritemap(sprite_one)) == False

def test_remove_sprite_that_does_not_exist(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]

    # Try and remove something that doesn't exist. This should throw a key
    # error, if it does not pytest will fail.
    with pytest.raises(KeyError):
        sprite_manager.remove_sprite(sprite_one)

def test_spritemap_changed_in_manager(baseline):
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
    image_path = str(Path(__file__).parent/"images/test3.png")
    new_spritemap = pygame.image.load(image_path)

    # Change spritemap
    sprite_one.spritemap = new_spritemap

    # Check Sprite's Key has changed in Sprite Manager
    assert (sprite_one in sprite_manager.sprites[old_spritemap]) == False

def test_sprites_new_key_in_manager(baseline):
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
    image_path = str(Path(__file__).parent/"images/test3.png")
    new_spritemap = pygame.image.load(image_path)

    # Change spritemap
    sprite_one.spritemap = new_spritemap

    # Check if Sprite's Key in Sprite Manager is new Sprite Map
    assert (sprite_one in sprite_manager.sprites[new_spritemap]) == True