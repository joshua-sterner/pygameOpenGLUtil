#!/usr/bin/env python

import pygame
from OpenGL.GL import *
from OpenGL.GL import shaders
import unittest
import OpenGLTestCase
import numpy as np
from ctypes import sizeof, c_float, c_void_p

def renderImage(image):
    # using resources in open gl generally follows the form of generate, bind, modify
    
    # Generate: request a buffer for our vertices
    vbo = glGenBuffers(1)
    
    # Bind: set the newly requested buffer as the active GL_ARRAY_BUFFER. 
    #   All subsequent modifications of GL_ARRAY_BUFFER will affect our vbo
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    # Modify: Tell OpenGL to load data into the buffer. 
    
    # I've added two more coordinates to each vertex here for determining the position within the texture.
    # These two additional coordinates are typically refered to as uv coordinates.
    # Also there are now two triangles that cover the entire viewport.
    vertex_data = np.array([-1, -1, 0, 0,  -1, 1, 0, 1,  1, 1, 1, 1,  -1, -1, 0, 0,  1, 1, 1, 1,  1, -1, 1, 0], np.float32)
    glBufferData(GL_ARRAY_BUFFER, vertex_data, GL_STATIC_DRAW)

    vertex_position_attribute_location = 0
    uv_attribute_location = 1
    
    glVertexAttribPointer(vertex_position_attribute_location, 2, GL_FLOAT, GL_FALSE, sizeof(c_float)*4, c_void_p(0))
    # vertex attributes need to be enabled
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(uv_attribute_location, 2, GL_FLOAT, GL_FALSE, sizeof(c_float)*4, c_void_p(sizeof(c_float)*2))
    glEnableVertexAttribArray(1)

    # Generate: request a texture
    image_texture = glGenTextures(1)

    # Bind: set the newly requested texture as the active GL_TEXTURE_2D.
    #   All subsequent modifications of GL_TEXTURE_2D will affect our texture (or how it is used)
    glBindTexture(GL_TEXTURE_2D, image_texture)
    
    
    width = image.get_width()
    height = image.get_height()

    # retrieve a byte string representation of the image.
    # The 3rd parameter tells pygame to return a vertically flipped image, as the coordinate system used
    # by pygame differs from that used by OpenGL
    image_data = pygame.image.tostring(image, "RGBA", True)

    # Modify: Tell OpenGL to load data into the image
    mip_map_level = 0
    glTexImage2D(GL_TEXTURE_2D, mip_map_level, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    # set the filtering mode for the texture
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    vertex_shader = shaders.compileShader("""
        #version 330
        layout(location = 0) in vec2 pos;
        layout(location = 1) in vec2 uvIn;
        out vec2 uv;
        void main() {
            gl_Position = vec4(pos, 0, 1);
            uv = uvIn;
        }
        """, GL_VERTEX_SHADER)

    fragment_shader = shaders.compileShader("""
        #version 330
        out vec4 fragColor;
        in vec2 uv;
        uniform sampler2D tex;
        void main() {
            fragColor = texture(tex, uv);
        }
    """, GL_FRAGMENT_SHADER)
    
    shader_program = shaders.compileProgram(vertex_shader, fragment_shader)

    # Enable alpha blending
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glUseProgram(shader_program)

    glDrawArrays(GL_TRIANGLES, 0, 6)

def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True
    
class OpenGLTestCaseExample2(OpenGLTestCase.OpenGLTestCase):

    def test_render_image(self):
        image = pygame.image.load("test.png")
        self.set_render_size(image.get_width(), image.get_height())
        
        renderImage(image)

        # wait for a key press to continue
        pygame.display.flip()
        wait_for_keypress()
        
        # load an image to compare the result with
        expected_image = pygame.image.load("test_render_image_expected.png")
        
        # convert expected image to a byte string with format RGB. Also flip the image vertically.
        #   (OpenGL uses a coordinate system where the y value increases from bottom to top, but pygame
        #   uses a coordinate system where y increases from top to bottom.)
        expected = pygame.image.tostring(expected_image, "RGB", True)

        # save the rendered image to test_results/OpenGLTestCaseExample/test_render_triangle.png
        # note that this must be called before any assert statements or it may not be reached if the test fails.
        self.save_rendered_image()
        
        self.assertEqual(expected, self.get_rendered_image())

    def test_render_image_overlay(self):
        image = pygame.image.load("colorGrid.png")
        self.set_render_size(image.get_width(), image.get_height())

        renderImage(image)

        overlayImage = pygame.image.load("test.png")
        renderImage(overlayImage)

        pygame.display.flip()
        wait_for_keypress()

if __name__ == "__main__":
    unittest.main()
    
