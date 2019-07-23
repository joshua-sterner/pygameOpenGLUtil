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

def get_rendered_image():
    """Returns the image rendered by opengl as a one-dimensional
    array of bytes in RGB format"""
    x, y, width, height = glGetInteger(GL_VIEWPORT)
    return glReadPixels(x, y, x + width, y + height, GL_RGB,
                        GL_UNSIGNED_BYTE)

def is_rendered_image(image):
    rendered_image_bytes = get_rendered_image()
    image_bytes = pygame.image.tostring(image, "RGB", True)
    return rendered_image_bytes == image_bytes

def save_image(filename):
    result = get_rendered_image()
    x, y, width, height = glGetInteger(GL_VIEWPORT)
    result_image = pygame.image.fromstring(result, (width, height), "RGB",                                            True)
    pygame.image.save(result_image, filename)
