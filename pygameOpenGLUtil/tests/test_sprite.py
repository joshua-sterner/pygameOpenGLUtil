import pygame
import pytest
from pygameOpenGLUtil import *
from pathlib import Path

def test_change_map_notifies_manager(baseline):
    #Assign variables for readability. 
    sprite_manager = baseline[0]
    sprite_one = baseline[1][0]
    sprite_two = baseline[1][1]
    #This sprite has a different sprite map then the other two.
    sprite_three = baseline[1][2]

    