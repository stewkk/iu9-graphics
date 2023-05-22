#!/usr/bin/env python3

import glfw
from OpenGL.GL import *

from dataclasses import dataclass
from copy import deepcopy
import time


@dataclass
class Point:
    x: int
    y: int

class PolygonDrawer:
    points = []
    pixel_buf = []
    window_width  = 1280
    window_height = 720
    enable_smoothing = True
    enable_displaying = False

    def mouseCallback(self, w, button, action, _):
        if action == glfw.PRESS and button == glfw.MOUSE_BUTTON_LEFT:
            x, y = glfw.get_cursor_pos(w)
            self.points.append(Point(int(x), self.window_height-int(y)))
            print(self.points)

    def keyboardCallback(self, w, key, _, action, __):
        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(w, True)
            elif key == glfw.KEY_D:
                if len(self.points) > 2:
                    self.enable_displaying = True
                    self.draw()
                else:
                    self.enable_displaying = False
            elif key == glfw.KEY_C:
                self.points = []
                self.enable_displaying = False
            elif key == glfw.KEY_S:
                self.enable_smoothing = not self.enable_smoothing
                self.draw()

    def sizeCallback(self, _, w, h):
        self.window_width, self.window_height = w, h
        glViewport(0, 0, w, h)
        self.draw()

    def display(self, _):
        glClear(GL_COLOR_BUFFER_BIT)

        if self.enable_displaying:
            glDrawPixels(self.window_width, self.window_height,
                GL_RED, GL_UNSIGNED_BYTE,
                         self.pixel_buf)

    def fill_to_right(self, p):
        for i in range(p.x+1, self.window_width):
            if self.pixel_buf[i+self.window_width*p.y] == 0:
                self.pixel_buf[i+self.window_width*p.y] = 255
            else:
                self.pixel_buf[i+self.window_width*p.y] = 0

    def fill_line(self, s, e):
        s_ = deepcopy(s)
        e_ = deepcopy(e)
        dx = abs(e_.x - s_.x)
        sx = 1 if s_.x < e_.x else -1
        dy = -abs(e_.y - s_.y)
        sy = 1 if s_.y < e_.y else -1
        error = dx + dy

        used = [False for _ in range(self.window_height)]

        while True:
            self.pixel_buf[s_.x+self.window_width*s_.y] = 255
            if not used[s_.y]:
                if (s_.y == s.y or s_.y == e.y):
                    if s_.y == self.mx or s_.y == self.mn:
                        self.fill_to_right(s_)
                    elif not self.used[s_.y]:
                        self.fill_to_right(s_)
                        self.used[s_.y] = True
                else:
                    self.fill_to_right(s_)
            used[s_.y] = True
            if s_.x == e_.x and s_.y == e_.y:
                break
            e2 = 2 * error
            if e2 >= dy:
                if s_.x == e_.x:
                    break
                error = error + dy
                s_.x = s_.x + sx
            if e2 <= dx:
                if s_.y == e_.y:
                    break
                error = error + dx
                s_.y = s_.y + sy

    def fill_polygon(self):
        self.pixel_buf = [0 for _ in range(self.window_height*self.window_width)]
        self.used = [False for _ in range(self.window_height)]
        self.mx = -10
        self.mn = 1000000
        for p in self.points:
            self.mx = max(self.mx, p.y)
            self.mn = min(self.mn, p.y)
        for i in range(len(self.points)):
            s = self.points[i]
            if i+1 == len(self.points):
                e = self.points[0]
            else:
                e = self.points[i+1]
            self.fill_line(s, e)

    def filtrate(self):
        pass

    def draw(self):
        self.fill_polygon()
        if self.enable_smoothing:
            self.filtrate()


def main():
    p = PolygonDrawer()

    glfw.init()

    window = glfw.create_window(p.window_width, p.window_height, "4", None, None)

    glfw.make_context_current(window)
    glfw.swap_interval(1)
    glfw.set_key_callback(window, p.keyboardCallback)
    glfw.set_mouse_button_callback(window, p.mouseCallback)
    glfw.set_framebuffer_size_callback(window, p.sizeCallback)

    w, h = glfw.get_framebuffer_size(window)
    p.sizeCallback(window, w, h)

    while not glfw.window_should_close(window):
        p.display(window)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main()

