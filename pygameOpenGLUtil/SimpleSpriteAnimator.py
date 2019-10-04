import time
from pygameOpenGLUtil import *

class SimpleSpriteAnimator:
    
    LOOP_MODE_NORMAL = 1
    LOOP_MODE_PING_PONG = 2

    def __init__(self):
        self.rate = 1.0
        self.running = False
        self._stop_next_frame = False
        self.loop = False
        self.loop_mode = self.LOOP_MODE_NORMAL
        self.reset_position_at_end = False

    def animate(self, sprite, time_delta):
        if (self._stop_next_frame):
            sprite.current_frame = 0
            self._stop_next_frame = False
        if (self.running):
            next_frame = sprite.current_frame + time_delta * self.rate * sprite.framerate
            if (next_frame > sprite.frames - 1):
                if (not self.loop):
                    next_frame = sprite.frames - 1
            sprite.current_frame = next_frame
    def play(self):
        self.running = True

    def pause(self):
        self.running = False

    def stop(self):
        self.running = False
        self._stop_next_frame = True
