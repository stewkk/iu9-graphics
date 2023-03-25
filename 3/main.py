#!/usr/bin/env python3

import glfw
from OpenGL.GL import *
from math import cos, sin, sqrt, asin, pi

xR, yR = 0.1, 0.1
h = 0.1
alpha, beta = 0, 0

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "LAB 3", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

def display(window):
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)

    glRotate(alpha, 0, 0, 1)
    glRotate(beta, 0, 1, 0)

    global h, xR, yR
    def cylinder():
        segments = 360
        segmentAngle = 2.0*pi / segments

        glBegin(GL_QUADS)
        for i in range(segments):
            x1 = xR * cos(i * segmentAngle)
            y1 = yR * sin(i * segmentAngle)
            x2 = xR * cos((i+1) * segmentAngle)
            y2 = yR * sin((i+1) * segmentAngle)

            glColor3f(0.0, 0.0, 1.0);
            glVertex3f(x1, y1, 0.0)
            glVertex3f(x2, y2, 0.0)
            glVertex3f(x2, y2, h)
            glVertex3f(x1, y1, h)

            glColor3f(1.0, 0.0, 0.0);
            glVertex3f(x1, y1, 0.0)
            glVertex3f(x2, y2, 0.0)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 0, 0)

            glColor3f(0.0, 1.0, 0.0);
            glVertex3f(x1, y1, h)
            glVertex3f(x2, y2, h)
            glVertex3f(0, 0, h)
            glVertex3f(0, 0, h)
        glEnd()
    cylinder()

    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action, mods):
    global xR, yR, h, alpha, beta
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_RIGHT:
            xR += 0.1
        elif key == glfw.KEY_LEFT:
            xR -= 0.1
        elif key == glfw.KEY_UP:
            yR += 0.1
        elif key == glfw.KEY_DOWN:
            yR -= 0.1
        elif key == glfw.KEY_W:
            h += 0.1
        elif key == glfw.KEY_D:
            h -= 0.1
        elif key == glfw.KEY_H:
            alpha -= 5
        elif key == glfw.KEY_J:
            beta -= 5
        elif key == glfw.KEY_K:
            beta += 5
        elif key == glfw.KEY_L:
            alpha += 5

if __name__ == "__main__":
    main()
