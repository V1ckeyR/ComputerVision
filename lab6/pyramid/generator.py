import random
from time import sleep

import numpy as np

from math import radians, cos, sin, tan, asin, sqrt
from lab6.pyramid.graphics import *
from lab6.pyramid.colors import COLORS


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


def isometric(figure):
    a = asin(tan(radians(30)))
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


def linear_bezier_curve(win, point1, point2, color, k):
    def b_curve(t, p1, p2): return (1 - t) * p1 + t * p2

    coordinates = []
    for a in np.arange(0, 1, k):
        x = b_curve(float(a), point1[0], point2[0])
        y = b_curve(float(a), point1[1], point2[1])
        Point(x, y).draw(win).setFill(color_rgb(*color))
        coordinates.append((x, y))

    return coordinates


def show_triangle(win, p1, p2, p3, color, visibility=True):
    k = 0.02 if visibility else 0.1

    linear_bezier_curve(win, p1, p2, color, k)
    linear_bezier_curve(win, p2, p3, color, k)
    line = linear_bezier_curve(win, p3, p1, color, k)

    if visibility:
        for p in line:
            linear_bezier_curve(win, p2, p, color, k)


def show_three_faces(win, p0, p1, p2, p3, color):
    show_triangle(win, p1, p2, p3, COLORS['white'], False)
    show_triangle(win, p0, p3, p1, color[2])
    show_triangle(win, p0, p2, p3, color[1])
    show_triangle(win, p0, p1, p2, color[0])


def show_two_faces(win, p0, p1, p2, p3, color):
    show_triangle(win, p0, p1, p3, color[2])
    show_triangle(win, p0, p1, p2, color[0])
    show_triangle(win, p1, p2, p3, COLORS['white'], False)
    show_triangle(win, p0, p2, p3, COLORS['white'], False)


def show_one_face(win, p0, p1, p2, p3, color):
    show_triangle(win, p0, p1, p2, color[1])
    show_triangle(win, p1, p2, p3, COLORS['white'], False)
    show_triangle(win, p0, p2, p3, COLORS['white'], False)
    show_triangle(win, p0, p1, p3, COLORS['white'], False)


def floating_horizon_algorithm(win, figure, color):
    points = [(figure[0, 0], figure[0, 1], figure[0, 2], 'a'),
              (figure[1, 0], figure[1, 1], figure[1, 2], 'b'),
              (figure[2, 0], figure[2, 1], figure[2, 2], 'c'),
              (figure[3, 0], figure[3, 1], figure[3, 2], 'o')]

    max_z = max([p[2] for p in points])
    nearest_point = [p for p in points if p[2] == max_z][-1]
    other_points = [p for p in points if p != nearest_point]

    # ???????? ?????????????????? ?????????? "??????????????????" ????????????????????, ???????????????????? ???????????? ??????????????,
    # ???? ???????????? 3 ??????????

    def if_point_inside_triangle(point, triangle):
        x_max = max([p[0] for p in triangle])
        x_min = min([p[0] for p in triangle])
        y_max = max([p[1] for p in triangle])
        y_min = min([p[1] for p in triangle])

        if x_min < point[0] < x_max and y_min < point[1] < y_max:
            return True

    if if_point_inside_triangle(nearest_point, other_points):
        show_three_faces(win, nearest_point, *other_points, color)
        return

    # ???????? ???????? ?????????? "??????????????????" ????????????????????, ???????????????????? ???? ???????????? ???????????????????? ??????????,
    # ???????? ???????????????????? ???????????????????? ?????????? ???? ????????-???????? ?????????? ??????????????????????
    # ???? ???????????? 1 ??????????
    # ?????????????????? ?????? ???????????? ??????????, ???? ???????????? "??????????????????" ??????????

    for other_point in other_points:
        other_triangle = [p for p in other_points if p != other_point]
        other_triangle.append(nearest_point)

        if other_point[0] == nearest_point[0] and other_point[1] == nearest_point[1]:
            show_one_face(win, *other_triangle, other_point, color)
            return

        if if_point_inside_triangle(other_point, other_triangle):
            show_one_face(win, *other_triangle, other_point, color)
            return

    # ???????? ????,
    # ???? ???????????? 2 ??????????
    # ???? ???????????????? ???????????? ?? ???????????????????? ?????????? ???? ???????????????????? ?????? ??????

    def get_vector_length(p1, p2): return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[0])**2)

    max_vector_length = max([get_vector_length(nearest_point, p) for p in other_points])
    farthest_point = [p for p in other_points if max_vector_length == get_vector_length(nearest_point, p)][0]
    show_two_faces(win, nearest_point, farthest_point, *[p for p in other_points if p != farthest_point], color)


def remove_pyramid(win, background):
    sleep(1)
    Rectangle(Point(0, 0), Point(win.width, 500)).draw(win).setFill('black')
    background(win)


def draw_pyramids(win, background):
    s = 50
    pyramid = np.array([
        [0, 0, 0, 1],
        [s, 0, 0, 1],
        [0, s, 0, 1],
        [0, 0, s, 1],
    ])

    pyramid = isometric(pyramid)
    pyramid = move(pyramid, np.array([250, 250, 0, 0]))

    floating_horizon_algorithm(win, pyramid, COLORS['red'])
    remove_pyramid(win, background)

    while True:
        for color_name in list(COLORS.keys())[1:]:
            next_point = np.append(np.random.randint(-500, 500, 3), [1])
            result = rotate(move(pyramid, next_point), radians(random.randint(10, 60)))
            while np.max(result) > 500 or np.min(result) < 0:
                next_point = np.append(np.random.randint(-100, 100, 3), [1])
                result = rotate(move(pyramid, next_point), radians(random.randint(10, 60)))

            pyramid = result
            floating_horizon_algorithm(win, pyramid, COLORS[color_name])
            remove_pyramid(win, background)
