import math
import random
from time import sleep

import numpy as np
from math import radians, cos, sin

from graphics import *


COLORS = {
    # 'black':  [(0, 0, 0),       (0, 0, 0),       (0, 0, 0)],
    # 'white':  [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    'pink':   [(128, 0, 86),    (255, 0, 171),   (255, 128, 213)],
    'red':    [(85, 0, 0),      (255, 0, 0),     (255, 128, 128)],
    'orange': [(128, 44, 0),    (255, 89, 0),    (255, 172, 128)],
    'yellow': [(128, 119, 0),   (255, 237, 0),   (255, 246, 128)],
    'green':  [(0, 91, 0),      (0, 181, 0),     (128, 218, 128)],
    'cyan':   [(0, 119, 128),   (0, 237, 255),   (128, 246, 255)],
    'blue':   [(0, 36, 86),     (0, 71, 171),    (128, 163, 213)],
    'violet': [(73, 37, 116),   (113, 58, 180),  (149, 107, 199)],
}


def move(figure,  point):
    for p in figure:
        p[-1] = 1

    return figure.dot(np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        point
    ]))


def isometric(figure):
    a = math.asin(math.tan(radians(30)))
    t1 = np.array([
        [cos(a), 0, -sin(a), 0],
        [0,      1,  0,      0],
        [sin(a), 0,  cos(a), 0],
        [0,      0,  0,      0]
    ])

    a = radians(45)
    t2 = np.array([
        [1,  0,      0,      0],
        [0,  cos(a), sin(a), 0],
        [0, -sin(a), cos(a), 0],
        [0,  0,      0,      0]
    ])

    return t2.dot(t1).dot(figure)


def color_change(i, count, start, end):
    new_color = []
    k = i / (count - i)
    for spector in range(3):
        candidate = int((start[spector] + k * end[spector]) / (k + 1))
        new_color.append(candidate if candidate <= 255 else 255)
    return new_color


def draw_line_raster(p1, p2, start_color, end_color):
    (x1, y1) = (p1[0], p1[1])
    (x2, y2) = (p2[0], p2[1])

    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    line = []
    Point(x, y).draw(win).setFill(color_rgb(*start_color))

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        line.append((x, y))

    for i in range(len(line)):
        (r, g, b) = color_change(i, len(line), start_color, end_color)
        Point(*line[i]).draw(win).setFill(color_rgb(r, g, b))

    return line


def draw_triangle(p1, p2, p3, start_color, end_color):
    draw_line_raster(p1, p2, start_color, end_color)
    draw_line_raster(p1, p3, start_color, end_color)
    for point in draw_line_raster(p3, p2, start_color, end_color)[:-2]:
        draw_line_raster(p1, point, start_color, end_color)


def show(figure, start_color, end_color):
    a = (figure[0, 0], figure[0, 1])
    b = (figure[1, 0], figure[1, 1])
    c = (figure[2, 0], figure[2, 1])
    o = (figure[3, 0], figure[3, 1])

    draw_triangle(o, c, a, end_color[2], start_color[2])  # light
    draw_triangle(b, o, a, start_color[1], end_color[1])  # color
    draw_triangle(b, c, o, start_color[0], end_color[0])  # dark
    sleep(1)


def remove_pyramid(figure):
    a = Point(figure[0, 0], figure[0, 1] - 10)
    b = Point(figure[1, 0] + 10, figure[1, 1] + 10)
    c = Point(figure[2, 0] - 10, figure[2, 1] + 10)
    Polygon(a, b, c).draw(win).setFill('black')


if __name__ == '__main__':
    win = GraphWin("Lab4", 500, 500)
    win.setBackground('black')
    s = 100

    pyramid = np.array([
        [0, 0, 0, 1],
        [s, 0, 0, 1],
        [0, s, 0, 1],
        [0, 0, s, 1],
    ])

    pyramid = isometric(pyramid)
    pyramid = move(pyramid, np.array([250, 250, 0, 0]))

    show(pyramid, COLORS['pink'], COLORS['blue'])
    remove_pyramid(pyramid)

    while True:
        next_point = np.append(np.random.randint(-500, 500, 3), [1])
        result = move(pyramid, next_point)
        while np.max(result) > 500 or np.min(result) < 0:
            next_point = np.append(np.random.randint(-500, 500, 3), [1])
            result = move(pyramid, next_point)

        pyramid = result
        show(pyramid, random.choice(list(COLORS.values())), random.choice(list(COLORS.values())))
        remove_pyramid(pyramid)
