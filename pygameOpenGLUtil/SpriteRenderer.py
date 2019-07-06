import pygame
import numpy as np
from ctypes import sizeof, c_float, c_void_p
from OpenGL.GL import *
from OpenGL.GL import shaders


class SpriteRenderer:
    """Renders the sprites in a SpriteManager"""
    def __init__(self, sprite_manager):
        self._sprite_manager = sprite_manager
        self._vbo = glGenBuffers(1)
        vertex_shader = shaders.compileShader("""
        #version 330
        layout(location = 0) in vec3 pos;
        layout(location = 1) in vec2 uvIn;
        out vec2 uv;
        void main() {
            gl_Position = vec4(pos, 1);
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
        self._shader_program = shaders.compileProgram(vertex_shader, fragment_shader)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        self._vertex_data = np.zeros(0, np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(c_float)*5, c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, sizeof(c_float)*5, c_void_p(sizeof(c_float)*3))
        glEnableVertexAttribArray(1)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def __del__(self):
        glDeleteBuffers(1, np.array(self._vbo))

    def render(self):
        self._width = pygame.display.get_surface().get_width()
        self._height = pygame.display.get_surface().get_height()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        glUseProgram(self._shader_program)
        for spritemap in self._sprite_manager.sprites:
            self._render_spritemap(spritemap)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def _render_spritemap(self, spritemap):
        spritemap.bind()
        sprites = self._sprite_manager.sprites[spritemap]
        self._upload_vertex_data(sprites)
        glDrawArrays(GL_TRIANGLES, 0, len(sprites)*6)
    
    def _upload_vertex_data(self, sprites):
        if (len(self._vertex_data) < len(sprites)*5*6):
            self._vertex_data = np.zeros(5*6*len(sprites), np.float32)
            self._update_vertex_data(sprites)
            glBufferData(GL_ARRAY_BUFFER, self._vertex_data, GL_DYNAMIC_DRAW)
        else:
            self._update_vertex_data(sprites)
            glBufferSubData(GL_ARRAY_BUFFER, 0, self._vertex_data)

    def _update_vertex_data(self, sprites):
        i = 0
        for sprite in sprites:
            spritemap_width = sprite.spritemap.width
            spritemap_height = sprite.spritemap.height
            spritemap_size = (spritemap_width, spritemap_height)
            pos = (sprite.x, sprite.y, sprite.z)
            uv = (sprite.spritemap_x, sprite.spritemap_y)
            self._set_vertex(i, pos, uv, (0, 0), spritemap_size)
            self._set_vertex(i+5, pos, uv, (sprite.width, 0), spritemap_size)
            self._set_vertex(i+10, pos, uv, (0, sprite.height), spritemap_size)
            self._set_vertex(i+15, pos, uv, (0, sprite.height), spritemap_size)
            self._set_vertex(i+20, pos, uv, (sprite.width, sprite.height), spritemap_size)
            self._set_vertex(i+25, pos, uv, (sprite.width, 0), spritemap_size)
            i += 5*6
    def _set_vertex(self, i, pos, uv, offset, spritemap_size):
        self._vertex_data[i] = 2.0*(pos[0]+offset[0])/self._width - 1.0
        self._vertex_data[i+1] = 1.0 - 2.0*(pos[1]+offset[1])/self._height
        self._vertex_data[i+2] = pos[2]
        self._vertex_data[i+3] = (uv[0]+offset[0])/spritemap_size[0]
        self._vertex_data[i+4] = 1.0 - (uv[1]+offset[1])/spritemap_size[1]
