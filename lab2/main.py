import math
import numpy as np

from graphics import *


def draw_rectangle(rect):
    f = Polygon(rect).draw(win)
    time.sleep(0.3)
    f.setOutline('white')


def transform_point(point, matrix):
    result = point.dot(matrix)
    return Point(result[0], result[1])


def rotate_matrix(angle): return np.array([
    [math.cos(angle), math.sin(angle), 0],
    [-math.sin(angle), math.cos(angle), 0],
    [0, 0, 1]])


def move_matrix(x, y): return np.array([
    [1, 0, 0],
    [0, 1, 0],
    [x, y, 1]])


def task1(original_rectangle):
    rectangle = original_rectangle

    def transformation(angle, operation='r+m', x=0, y=0):
        transform_matrix = rotate_matrix(angle) if operation == 'r' else rotate_matrix(angle).dot(move_matrix(x, y))
        return [transform_point(np.array([point.x, point.y, 1]), transform_matrix) for point in rectangle]

    while True:
        if max(max([[point.x, point.y] for point in rectangle])) < 500:
            draw_rectangle(rectangle)
            rectangle = transformation(theta, 'r')
            draw_rectangle(rectangle)
            rectangle = transformation(alpha, x=dx, y=dy)
        else:
            rectangle = original_rectangle


def task2(original_rectangle):
    rectangle = original_rectangle

    def to_polygon(rect): return [Point(point[0], point[1]) for point in rect]

    def rotate_operation(angle): return rectangle.dot(rotate_matrix(angle))

    def rotate_and_move_operation(angle, x, y): return rectangle.dot(rotate_matrix(angle)).dot(move_matrix(x, y))

    while True:
        if max(max([[point[0], point[1]] for point in rectangle])) < 500:
            draw_rectangle(to_polygon(rectangle))
            rectangle = rotate_operation(theta)
            draw_rectangle(to_polygon(rectangle))
            rectangle = rotate_and_move_operation(alpha, dx, dy)
        else:
            rectangle = original_rectangle


def task3(original_rectangle):
    rectangle = original_rectangle

    def rotate_operation(angle):
        def point(x, y):
            return Point(x * math.cos(angle) - y * math.sin(angle),
                         x * math.sin(angle) + y * math.cos(angle))

        return [point(p.x, p.y) for p in rectangle]

    def rotate_and_move(angle, sx, sy):
        def point(x, y):
            return Point(x * math.cos(angle) - y * math.sin(angle) + sx,
                         x * math.sin(angle) + y * math.cos(angle) + sy)

        return [point(p.x, p.y) for p in rectangle]

    while True:
        if max(max([[point.x, point.y] for point in rectangle])) < 500:
            draw_rectangle(rectangle)
            rectangle = rotate_operation(theta)
            draw_rectangle(rectangle)
            rectangle = rotate_and_move(alpha, dx, dy)
        else:
            rectangle = original_rectangle


if __name__ == '__main__':
    win = GraphWin("Lab2", 500, 500)
    win.setBackground('white')
    a, b = 100, 200
    alpha, theta = 0.45, -0.4
    dx, dy = 40, 30

    task1([Point(0, 0), Point(a, 0), Point(a, b), Point(0, b)])

    task2(np.array([
        [0, 0, 1],
        [a, 0, 1],
        [a, b, 1],
        [0, b, 1]
    ]))

    task3([Point(0, 0), Point(a, 0), Point(a, b), Point(0, b)])
