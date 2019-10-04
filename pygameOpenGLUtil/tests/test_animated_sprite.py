import pygame
import pytest
from pygameOpenGLUtil import *

class MockAnimationHandler():
    def __init__(self, change_frame=False):
        self.animate_called = False
        self.animate_args = ()
        self.change_frame = change_frame
    def animate(self, sprite, time):
        self.animate_called = True
        self.animate_args = (sprite, time)
        if (self.change_frame):
            sprite.current_frame += 1


def test_animated_sprite_animate_calls_animation_handler():
    
    animation_handler = MockAnimationHandler()
    sprite = AnimatedSprite(None, (0, 0), (1, 1), 4, 24, animation_handler)
    sprite.animate(123.456)

    assert animation_handler.animate_called
    assert animation_handler.animate_args[0] == sprite
    assert animation_handler.animate_args[1] == 123.456
