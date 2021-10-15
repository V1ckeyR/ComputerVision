import random
from time import sleep

import numpy as np
from math import radians, cos, sin

from graphics import *


COLORS = {
    'black':  [(0, 0, 0),       (0, 0, 0),       (0, 0, 0),       (0, 0, 0)],
    'pink':   [(255, 0, 171),   (255, 85, 199),  (255, 128, 213), (255, 170, 227)],
    'yellow': [(255, 237, 255), (255, 246, 128), (255, 242, 64),  (255, 251, 191)],
    'cyan':   [(0, 237, 255),   (128, 246, 255), (64, 242, 255),  (191, 251, 255)],
    'red':    [(255, 0, 0),     (255, 128, 128), (255, 64, 64),   (255, 191, 191)],
}


def uniform_coordinates(figure):
    for point in figure:
        point[-1] = 1


def move(figure,  point):
    uniform_coordinates(figure)
    return figure.dot(np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        point
    ]))


def rotate_x(figure, a):
    uniform_coordinates(figure)
    return figure.dot(np.array([
        [1,  0, 0, 0],
        [0,  cos(a), sin(a), 0],
        [0, -sin(a), cos(a), 0],
        [0,  0,      0,      1]
    ]))


def rotate_y(figure, a):
    uniform_coordinates(figure)
    return figure.dot(np.array([
        [cos(a), 0, -sin(a), 0],
        [0,      1,  0,      0],
        [sin(a), 0,  cos(a), 0],
        [0,      0,  0,      1]
    ]))


def rotate(figure, a): return rotate_y(rotate_x(figure, a), a)


def show(figure, color):
    o = Point(figure[0, 0], figure[0, 1])
    a = Point(figure[1, 0], figure[1, 1])
    b = Point(figure[2, 0], figure[2, 1])
    c = Point(figure[3, 0], figure[3, 1])

    t = Polygon(o, a, b).draw(win)
    t.setFill(color_rgb(*color[0]))

    t = Polygon(o, c, b).draw(win)
    t.setFill(color_rgb(*color[1]))

    t = Polygon(o, a, c).draw(win)
    t.setFill(color_rgb(*color[2]))

    Polygon(c, a, b).draw(win)
    sleep(1)


def isometric(figure):
    a = radians(120)
    t1 = np.array([
        [cos(a), 0, -sin(a), 0],
        [0,      1,  0,      0],
        [sin(a), 0,  cos(a), 0],
        [0,      0,  0,      0]
    ])

    t2 = np.array([
        [1,  0,      0,      0],
        [0,  cos(a), sin(a), 0],
        [0, -sin(a), cos(a), 0],
        [0,  0,      0,      0]
    ])

    return figure.dot(t1).dot(t2)


if __name__ == '__main__':
    win = GraphWin("Lab3", 500, 500)
    win.setBackground('black')
    s = 50

    pyramid = np.array([
        [0, 0, 0, 1],  # O
        [s, 0, 0, 1],  # A
        [0, s, 0, 1],  # B
        [0, 0, s, 1]   # C
    ])

    pyramid = isometric(pyramid)
    pyramid = move(pyramid, np.array([250, 250, 0, 0]))

    show(pyramid, COLORS['red'])
    show(pyramid, COLORS['black'])

    while True:
        for k in list(COLORS.keys())[1:]:
            next_point = np.append(np.random.randint(-500, 500, 3), [1])
            result = rotate(move(pyramid, next_point), radians(random.randint(10, 60)))
            while np.max(result) > 500 or np.min(result) < 0:
                next_point = np.append(np.random.randint(-100, 100, 3), [1])
                result = rotate(move(pyramid, next_point), radians(random.randint(10, 60)))

            pyramid = result
            show(pyramid, COLORS[k])
            show(pyramid, COLORS['black'])
