import pyglet
from pyglet.window import mouse, key
import numpy as np
from matrix import matrix


class render(object):
    window = pyglet.window.Window(fullscreen=True)
    vertex_list = None

    def __init__(self, space, colors):
        self.space = space
        self.colors = colors
        self.amount = self.space.amount
        self.mat = matrix(self.space.field)

        render.vertex_list = pyglet.graphics.vertex_list(self.space.amount, 'v2f/stream', 'c3B/static')
        render.vertex_list.vertices = list(self.mat.positions.flatten())
        render.vertex_list.colors = colors

        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        self.mat.tick(.5)
        render.vertex_list.vertices = list(self.mat.positions.flatten())

    @window.event
    def on_draw():
        render.window.clear()
        render.vertex_list.draw(pyglet.gl.GL_POINTS)

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.LEFT:
            pass
        elif symbol == key.RIGHT:
            pass
        elif symbol == key.UP:
            pass
        elif symbol == key.DOWN:
            pass

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            pass

        if button == mouse.RIGHT:
            pass
