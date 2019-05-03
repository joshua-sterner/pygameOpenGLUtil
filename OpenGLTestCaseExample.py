#!/usr/bin/env python

import pygame
from OpenGL.GL import *
from OpenGL.GL import shaders
import unittest
import OpenGLTestCase
import numpy as np
from ctypes import sizeof, c_float, c_void_p

def renderTriangle():
    # using resources in open gl generally follows the form of generate, bind, modify
    
    # Generate: request a buffer for our vertices
    vbo = glGenBuffers(1) # vbo stands for vertex buffer object

    # Bind: set the newly requested buffer as the active GL_ARRAY_BUFFER. 
    #   All subsequent modifications of GL_ARRAY_BUFFER will affect our vbo
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    # Modify: Tell OpenGL to load data into the buffer. 
    
    # Create an array of vertices to load into the VBO
    vertex_data = np.array([-1, -1, 0, 1, 1, -1], np.float32)
    # GL_STATIC_DRAW tells OpenGL that we will not be updating this data very often if at all.
    glBufferData(GL_ARRAY_BUFFER, vertex_data, GL_STATIC_DRAW)
    # Tell OpenGL how our vertices are formatted.
    number_of_values_per_vertex = 2
    size_of_vertex_in_bytes = sizeof(c_float)*2
    offset_into_vertex_data = c_void_p(0)
    glVertexPointer(number_of_values_per_vertex, GL_FLOAT, size_of_vertex_in_bytes, offset_into_vertex_data)

    # Modern OpenGL Requires a minimum of a vertex shader and a fragment shader rendering
    vertex_shader = shaders.compileShader("""
        #version 330
        in vec2 pos;
        void main() {
            gl_Position = vec4(pos, 0, 1);   
        }
        """, GL_VERTEX_SHADER)

    fragment_shader = shaders.compileShader("""
        #version 330
        out vec4 fragColor;
        void main() {
            fragColor = vec4(0.0, 1.0, 0.0, 1.0);
        }
    """, GL_FRAGMENT_SHADER)
    
    shader_program = shaders.compileProgram(vertex_shader, fragment_shader)

    # Vertex arrays must be enabled before attempting to render from one
    glEnableClientState(GL_VERTEX_ARRAY)
    
    # Tell OpenGL to use the created shader program
    glUseProgram(shader_program)

    # Actually render the triangle
    glDrawArrays(GL_TRIANGLES, 0, 3)

def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True
    
class OpenGLTestCaseExample(OpenGLTestCase.OpenGLTestCase):

    def test_render_triangle(self):
        # prepare to render
        self.set_render_size(128, 128)
    
        # attempt to render a green triangle
        renderTriangle()

        # wait for a key press to continue
        pygame.display.flip()
        wait_for_keypress()
        
        # load an image to compare the result with
        expected_image = pygame.image.load("test_render_triangle_expected.png")
        # convert expected image to a byte string with format RGB. Also flip the image vertically.
        #   (OpenGL uses a coordinate system where the y value increases from bottom to top, but pygame
        #   uses a coordinate system where y increases from top to bottom.)
        expected = pygame.image.tostring(expected_image, "RGB", True)

        self.assertEqual(expected, self.get_rendered_image())
    
        # save the rendered image to test_results/OpenGLTestCaseExample/test_render_triangle.png
        self.save_rendered_image()

if __name__ == "__main__":
    unittest.main()
    
