import time
from pygameOpenGLUtil import *

class SimpleSpriteAnimator:
    def __init__(self):
        self.rate = 1.0
        self.running = False
        self._stop_next_frame = False

    def animate(self, sprite, time_delta):
        if (self._stop_next_frame):
            sprite.current_frame = 0
            self._stop_next_frame = False
        if (self.running):
            sprite.current_frame += time_delta * self.rate * sprite.framerate

    def play(self):
        self.running = True

    def pause(self):
        self.running = False

    def stop(self):
        self.running = False
        self._stop_next_frame = True
