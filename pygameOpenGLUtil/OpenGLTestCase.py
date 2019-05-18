#!/usr/bin/env python

import pygame
from OpenGL.GL import *
from OpenGL.GL import shaders
import unittest
import inspect
import os
import os.path


class OpenGLTestCase(unittest.TestCase):
    """This class adds functionality for testing opengl rendering to
    unittest.TestCase"""

    def set_render_size(self, width, height):
        """Resets pygame and the opengl context, then creates a pygame
        window and opengl viewport of the requested size."""
        pygame.quit()
        pygame.init()
        self.size = (width, height)
        pygame.display.set_mode(self.size, pygame.OPENGL | pygame.DOUBLEBUF |
                                pygame.HWSURFACE)
        glViewport(0, 0, width, height)

    def get_rendered_image(self):
        """Returns the image rendered by opengl as a one-dimensional
        array of bytes in RGB format"""
        return glReadPixels(0, 0, self.size[0], self.size[1], GL_RGB,
                            GL_UNSIGNED_BYTE)

    def save_rendered_image(self, save_dir="test_results"):
        """Saves the image rendered by opengl to the file
        save_dir/<test_class_name>/<test_name> where <test_class_name> is
        replaced by the name of the class in which the tests were written, and
        <test_name> is replaced by the name of the test method. This assumes
        that save_rendered_image is being called from within the test method
        directly."""
        viewport_dimensions = glGetIntegerv(GL_VIEWPORT)
        width = viewport_dimensions[2]-viewport_dimensions[0]
        height = viewport_dimensions[3]-viewport_dimensions[1]
        result = self.get_rendered_image()
        result_image = pygame.image.fromstring(result, (width, height), "RGB",
                                               True)
        test_class = inspect.currentframe().f_locals["self"].__class__
        test_class_name = test_class.__name__
        test_name = inspect.currentframe().f_back.f_code.co_name
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        if not os.path.exists(save_dir+"/"+test_class_name):
            os.mkdir(save_dir+"/"+test_class_name)
        result_image_path = save_dir+"/"+test_class_name+"/"+test_name+".png"
        pygame.image.save(result_image, result_image_filename)
