import math
import turtle
from .CircleAngles import CircleAngles


COLORS = {
    'violet': (145, 35, 243),
    'blue': (0, 186, 254),
    'green': (0, 255, 0),
    'yellow': (255, 242, 0),
    'red': (255, 55, 55),
    'white': (255, 255, 255)
}

COLORS_LIST = list(COLORS.values())
ANGELS_FOR_CIRCLE = list(CircleAngles())


def move_point(p, *, x, y):
    p.penup()
    p.goto(x, y)
    p.pendown()


def square(p, size, color=COLORS['white']):
    p.color(color)
    p.fillcolor(color)
    p.begin_fill()
    for _ in range(4):
        p.forward(size)
        p.right(90)
    p.end_fill()


def draw_squares(p, size, dx):
    size += 4 * 2 * dx
    for n in range(5):
        color = COLORS_LIST[n]
        square(p, size, color)
        (x, y) = p.position()
        move_point(p, x=x+dx, y=y-dx)
        size -= 2 * dx


def draw_circles(p, radius, dx):
    (xc, yc) = p.position()
    radius += 4 * dx
    for n in range(5):
        p.color(COLORS_LIST[n])
        for a in ANGELS_FOR_CIRCLE:
            move_point(p, x=xc, y=yc)
            x = xc + radius * math.cos(a)
            y = yc + radius * math.sin(a)
            p.goto(x, y)
        radius -= dx


def task1():
    """необхідно розробити блок-схему алгоритму та програму,
     що реалізує побудову графічних фігур: 5 кілець і 5 квадратів.
     Фігури розташовані в одному графічному вікні.
     Колір фігур однаковий. Поле між кільцями різної заливки.
     1 фігура малюється лініями, 2 вбудованими засобами.
    """

    win = turtle.Screen()
    win.title("Task1")
    win.colormode(255)

    point = turtle.Turtle()
    point.speed(0)
    point.pensize(3)

    r = 50  # radius of smallest circle
    s = 2*r  # size of smallest square
    d = 20   # width between figures
    a = 10   # from center to largest figure

    move_point(point, x=-1*(r+4*d+a), y=0)
    draw_circles(point, r, d)

    move_point(point, x=s/2+4*d+a, y=s/2+4*d)
    draw_squares(point, s, d)

    turtle.done()


def draw_figure_using_lines(p, r, *, xc, yc, width, delta, is_colorful):
    def draw_ring(x, y):
        for a in ANGELS_FOR_CIRCLE:
            x1 = x + r * math.cos(a)
            y1 = y + r * math.sin(a)
            x2 = x + (r - width) * math.cos(a)
            y2 = y + (r - width) * math.sin(a)

            move_point(p, x=x1, y=y1)
            p.goto(x2, y2)

    if is_colorful:
        p.color(COLORS['blue'])
    draw_ring(xc, yc + r - delta)

    if is_colorful:
        p.color(COLORS['violet'])
    draw_ring(xc, yc - r + delta)

    if is_colorful:
        p.color(COLORS['red'])
    draw_ring(xc + r - delta, yc)

    if is_colorful:
        p.color(COLORS['yellow'])
    draw_ring(xc - r + delta, yc)


def draw_figure_using_polygons(p, *, xc, yc, delta, is_colorful):
    def polygon(n):
        for _ in range(n):
            p.forward(1)
            p.right(360 / n)

    p.color('black')
    p.pensize(15)
    r = 75

    if is_colorful:
        p.color(COLORS['blue'])

    move_point(p, x=xc, y=yc + 2 * r - delta)
    polygon(500)

    if is_colorful:
        p.color(COLORS['violet'])
    move_point(p, x=xc, y=yc + delta)
    polygon(500)

    if is_colorful:
        p.color(COLORS['red'])
    move_point(p, x=xc - r + delta, y=yc + r)
    polygon(500)

    if is_colorful:
        p.color(COLORS['yellow'])
    move_point(p, x=xc + r - delta, y=yc + r)
    polygon(500)


def task2():
    """
    Фігуру побудувати двома способами:
    1. В якості базових примітивів використати лінії;
    2. В якості базових примітивів використати багатокутник.
    Передбачити монохромний та кольоровий варіант із заливкою з різним кольором та різнокольоровими обмежувальними
    лініями. Кольорову гаму обрати за одним із відомих способів комбінації кольорів.
    """

    win = turtle.Screen()
    win.title("Task2")
    win.colormode(255)

    point = turtle.Turtle()
    point.speed(0)
    point.pensize(3)

    radius = 120
    w = 15
    d = 30
    between = 250

    draw_figure_using_lines(point, radius, xc=-1 * between, yc=-1 * between, width=w, delta=d, is_colorful=False)
    draw_figure_using_lines(point, radius, xc=-1 * between, yc=between, width=w, delta=d, is_colorful=True)

    draw_figure_using_polygons(point, xc=between, yc=-1 * between, delta=d/2, is_colorful=False)
    draw_figure_using_polygons(point, xc=between, yc=between, delta=d/2, is_colorful=True)

    turtle.done()


def draw_axes(p, x, y, size):
    move_point(p, x=x, y=y)
    p.color('black')

    for _ in range(4):
        p.forward(size)
        p.right(90)

    move_point(p, x=x, y=y-size/2)
    p.forward(size)


def draw_graphic(p, rule, step=0.01, max_x=300, *, xc, yc):
    x0 = 0
    xs = []
    coo = []
    k = 80

    while x0*k < max_x:
        xs.append(x0)
        x0 += step

    move_point(p, x=xc, y=yc)
    for x in xs:
        try:
            p.goto(x * k + xc, rule(x) * k + yc)
            coo.append((x * k + xc, rule(x) * k + yc))
        except ValueError:
            break
    return coo


def draw_graphic_using_coordinates(p, coo, color, *, xc, yc, dx, dy):
    move_point(p, x=xc, y=yc)
    p.color(color)
    for pair in coo:
        x0, y0 = pair
        p.goto(x0 + dx, y0 + dy)


def task3():
    """
    скрипт, що реалізує побудову та відображення трьох окремих графіків епюрів тестових сигналів та четвертий графік з
    сумісним відображенням епюрів усіх трьох сигналів
    Центр координатної сітки розташований в центрі лівої межі графічного вікна. Координатні осі позначені надписами.
    Графіки різних сигналів мають різний колір.
    """

    a = 17

    def first(x): return math.acos(x)

    def second(x): return a * 0.01 * math.atan(x)

    def third(x): return a * 0.01 * math.asin(x)

    win = turtle.Screen()
    win.title("Task3")
    win.colormode(255)

    point = turtle.Turtle()
    size = 300
    delta = 50
    delta_for_axes = size + delta

    draw_axes(point, -delta_for_axes, delta_for_axes, size)
    point.color(COLORS['red'])
    coo1 = draw_graphic(point, first, xc=-delta_for_axes, yc=delta_for_axes-size/2)

    draw_axes(point, delta, delta_for_axes, size)
    point.color(COLORS['green'])
    coo2 = draw_graphic(point, second, xc=delta, yc=delta_for_axes-size/2)

    draw_axes(point, -delta_for_axes, -delta, size)
    point.color(COLORS['blue'])
    coo3 = draw_graphic(point, third, xc=-delta_for_axes, yc=-delta-size/2)

    draw_axes(point, delta, -delta, size)
    draw_graphic_using_coordinates(point, coo1, COLORS['red'],
                                   xc=delta, yc=-delta-size/2,
                                   dx=delta+delta_for_axes, dy=-delta-delta_for_axes)

    draw_graphic_using_coordinates(point, coo2, COLORS['green'],
                                   xc=delta, yc=-delta-size/2,
                                   dx=delta-delta, dy=-delta-delta_for_axes)

    draw_graphic_using_coordinates(point, coo3, COLORS['blue'],
                                   xc=delta, yc=-delta-size/2,
                                   dx=delta+delta_for_axes, dy=-delta+delta)

    turtle.done()
