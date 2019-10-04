import pytest
from pygameOpenGLUtil import *

class MockAnimatedSprite:
    def __init__(self, frames, framerate):
        self.frames = frames
        self.framerate = framerate
        self.current_frame = 0

def test_animation_paused_by_default():
    sprite = MockAnimatedSprite(8, 24)
    animator = SimpleSpriteAnimator()
    animator.animate(sprite, 1.5/24)
    assert sprite.current_frame == 0
    assert animator.running == False

def test_play_sets_running_true():
    animator = SimpleSpriteAnimator()
    animator.play()
    assert animator.running == True

def test_pause_sets_running_false():
    animator = SimpleSpriteAnimator()
    animator.pause()
    assert animator.running == False

def test_stop_sets_running_false():
    animator = SimpleSpriteAnimator()
    animator.stop()
    assert animator.running == False

def test_stop_resets_current_frame_on_next_animate():
    sprite = MockAnimatedSprite(8, 24)
    sprite.current_frame = 4
    animator = SimpleSpriteAnimator()
    animator.stop()
    animator.animate(sprite, 1.2)
    assert sprite.current_frame == 0

def test_stop_does_not_reset_current_frame_on_second_animate():
    sprite = MockAnimatedSprite(8, 24)
    sprite.current_frame = 4
    animator = SimpleSpriteAnimator()
    animator.stop()
    animator.animate(sprite, 1.2)
    sprite.current_frame = 3
    animator.animate(sprite, 3.4)
    assert sprite.current_frame == 3

def test_play_animate():
    sprite = MockAnimatedSprite(8, 24)
    animator = SimpleSpriteAnimator()
    animator.play()
    animator.animate(sprite, 0.5/24)
    assert sprite.current_frame == pytest.approx(0.5)
    animator.animate(sprite, 0.51/24)
    assert sprite.current_frame == pytest.approx(1.01)
    animator.animate(sprite, 3.01/24)
    assert sprite.current_frame == pytest.approx(4.02)

def test_play_animate_0_7_rate():
    sprite = MockAnimatedSprite(8, 24)
    animator = SimpleSpriteAnimator()
    animator.rate = 0.7
    animator.play()
    animator.animate(sprite, 0.5/(24*0.7))
    assert sprite.current_frame == pytest.approx(0.5)
    animator.animate(sprite, 0.51/(24*0.7))
    assert sprite.current_frame == pytest.approx(1.01)
    animator.animate(sprite, 3.01/(24*0.7))
    assert sprite.current_frame == pytest.approx(4.02)

def test_pause():
    sprite = MockAnimatedSprite(8, 24)
    animator = SimpleSpriteAnimator()
    animator.play()
    animator.animate(sprite, 0.5/(24*0.7))
    #TODO finish this...

def test_loop_false():
    sprite = MockAnimatedSprite(8, 24)
    animator = SimpleSpriteAnimator()
    sprite.current_frame = 6
    animator.play()
    animator.animate(sprite, 1.5/24)
    assert sprite.current_frame == 7
