import math

from lab6.pyramid.colors import COLORS
from lab6.pyramid.graphics import *


def cantor(win, position, color, length, distance=10, iteration=7):
    figure = "F"
    rule = {"F": "F-F", "-": "---"}
    start, height = position

    def draw_figure(x, h):
        x1 = start
        x2 = x1 + x
        for part in figure:
            if part == "F":
                Line(Point(x1, h), Point(x2, h)).draw(win).setFill(color)
            x1 = x2
            x2 = x1 + x

    for i in range(iteration):
        draw_figure(length, height)
        length /= 3
        height += distance
        figure = "".join(rule[part] if part in rule else part for part in figure)


def sierpinski(win, position, color, size=300, iteration=6):
    x1, y1 = position
    x2, y2 = x1 + size, y1
    x3, y3 = x1 + size / 2, y1 - size * math.sqrt(3) / 2
    triangle = [Point(x1, y1), Point(x2, y2), Point(x3, y3)]
    Polygon(triangle).draw(win).setFill(color)

    def draw_figure(t, i):
        if not i:
            return

        p1, p2, p3 = t
        pc1 = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
        pc2 = Point((p1.x + p3.x) / 2, (p1.y + p3.y) / 2)
        pc3 = Point((p2.x + p3.x) / 2, (p2.y + p3.y) / 2)

        Polygon(pc1, pc2, pc3).draw(win).setFill('white')
        draw_figure([p1, pc1, pc2], i - 1)
        draw_figure([p2, pc1, pc3], i - 1)
        draw_figure([p3, pc2, pc3], i - 1)

    draw_figure(triangle, iteration)


def lake(win):
    cantor(win, (0, 430), color_rgb(*COLORS['blue'][1]), win.width)
    cantor(win, (win.width / 3, 440), color_rgb(*COLORS['cyan'][1]), win.width / 3)
    cantor(win, (win.width / 9, 450), color_rgb(*COLORS['cyan'][1]), win.width / 9)
    cantor(win, (win.width / 9 * 4, 450), color_rgb(*COLORS['white']), win.width / 9)
    cantor(win, (win.width / 9 * 7, 450), color_rgb(*COLORS['cyan'][1]), win.width / 9)


def mountains(win):
    sierpinski(win, (230, 420), color_rgb(*COLORS['cyan'][1]))
    sierpinski(win, (0, 420), color_rgb(*COLORS['orange'][1]), size=200, iteration=5)
    sierpinski(win, (140, 420), color_rgb(*COLORS['red'][1]), size=100, iteration=4)
