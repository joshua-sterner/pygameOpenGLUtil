import pygame
from OpenGL.GL import *
from OpenGL.GL import shaders

def openGLTestSetup(width, height):
    """Resets pygame and the opengl context, then creates a pygame
    window and opengl viewport of the requested size."""
    pygame.quit()
    pygame.init()
    pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF |
                            pygame.HWSURFACE)
    glViewport(0, 0, width, height)

