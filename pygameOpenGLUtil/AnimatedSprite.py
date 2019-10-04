import time
from pygameOpenGLUtil import *

class AnimatedSprite(Sprite):
    def __init__(self, sprite_map, spritemap_pos, size, frames, framerate, animation_handler):
        super().__init__(sprite_map, spritemap_pos, size)
        self.frames = frames # The total number of frames in this animation.
        self.framerate = framerate
        self.current_frame = 0.0 # The current frame of the animation. May have a fractional component.
        self.animation_handler = animation_handler # Responsible for animation playback, etc
        # must have an animate(sprite, time_delta) method that updates
        # sprite.current_frame as needed

    def animate(self, time_delta):
        """Calls the animation handler."""
        self.animation_handler.animate(self, time_delta)
