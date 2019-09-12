import time
from pygameOpenGLUtil import *

class AnimatedSprite(Sprite):
    def __init__(self, sprite_map, spritemap_pos, size, frames, framerate, animation_handler):
        super().__init__(sprite_map, spritemap_pos, size)
        self.frames = frames # The total number of frames in this animation
        self.framerate = framerate
        self.current_frame = 0
        # using the monotonic clock so that animation_handler can assume a positive time delta
        self.last_frame_change_time = time.monotonic()
        self.animation_handler = animation_handler # Responsible for animation playback, etc
        # must have an animate(sprite, time) method that updates
        # sprite.current_frame as needed

    def animate(self, time):
        """Calls the animation handler, and updates last_frame_change_time if current_frame changed.
           time is expected to be a value returned by the monotonic clock (time.monotonic())."""
        frame = self.current_frame
        self.animation_handler.animate(self, time)
        if (self.current_frame != frame):
            self.last_frame_change_time = time

