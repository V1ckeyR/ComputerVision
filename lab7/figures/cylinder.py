import math
from OpenGL.GL import *


def draw_cylinder(radius, height, num_slices, move):
    r = radius
    h = height
    n = float(num_slices)

    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle) + move[0]
        y = r * math.sin(angle) + move[1]
        pt = (x, y)
        circle_pts.append(pt)

    glBegin(GL_TRIANGLE_FAN)  # drawing the back circle
    glColor(1, 0, 0)
    glVertex(move[0], move[1], h/2)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)  # drawing the front circle
    glColor(0, 0, 1)
    glVertex(move[0], move[1], h/2)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)  # draw the tube
    glColor(0, 1, 0)
    for (x, y) in circle_pts:
        z = h/2
        glVertex(x, y, z)
        glVertex(x, y, -z)
    glEnd()
