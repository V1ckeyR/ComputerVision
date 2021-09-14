import math

from .CircleAngles import CircleAngles
from .graphics import *

ANGELS_FOR_CIRCLE = list(CircleAngles())


def draw_squares(window, size):
    dx = size * 6
    k = 1
    for i in range(5):
        dx -= size
        k = k * -1
        sq = Rectangle(Point(375-dx, 250-dx), Point(375+dx, 250+dx))
        sq.setFill(color_rgb(130 - k * dx, 2 * dx, 130 + k * dx))
        sq.draw(window)


def draw_circle(window, size, color, xc=125, yc=250):
    center = Point(xc, yc)

    for a in ANGELS_FOR_CIRCLE:
        x = xc + size * math.cos(a)
        y = yc + size * math.sin(a)

        line = Line(center, Point(x, y))
        line.setFill(color)
        line.draw(window)


def draw_circles(window, size):
    dx = size * 6
    k = 1

    for i in range(4):
        dx -= size
        k = k * -1
        draw_circle(window, dx, color_rgb(130 - k * dx, 2 * dx, 130 + k * dx))

    draw_circle(window, size, color_rgb(130, 0, 130))


def draw_ring_using_lines(window, size, width, color, xc, yc):
    for a in ANGELS_FOR_CIRCLE:
        x1 = xc + size * math.cos(a)
        y1 = yc + size * math.sin(a)
        x2 = xc + (size - width) * math.cos(a)
        y2 = yc + (size - width) * math.sin(a)

        line = Line(Point(x2, y2), Point(x1, y1))
        line.setFill(color)
        line.draw(window)


def draw_ring_using_polygon(window, size, width, color, xc, yc):
    points = []

    for a in ANGELS_FOR_CIRCLE:
        x1 = xc + size * math.cos(a)
        y1 = yc + size * math.sin(a)
        x2 = xc + (size - width) * math.cos(a)
        y2 = yc + (size - width) * math.sin(a)
        points.extend([Point(x1, y1), Point(x2, y2)])

    p = Polygon(points)
    p.setOutline(color)
    p.draw(window)


def draw_axes():
    win = GraphWin("Lab1 Task3", 1000, 500)

    ox = Line(Point(0, 250), Point(1000, 250))
    ox.draw(win)
    label = Text(Point(990, 260), 'x')
    label.draw(win)

    oy = Line(Point(4, 0), Point(4, 500))
    oy.draw(win)
    label = Text(Point(10, 10), 'y')
    label.draw(win)
    return win


def get_xs(window, step=0.01):
    x0 = 0
    xs = []
    max_x = window.getWidth()

    while x0 < max_x:
        xs.append(x0)
        x0 += step

    return xs


def get_coordinates(rule, xs):
    coo = []
    for x in xs:
        try:
            if x * 100 + 4 > 1000:  # to scale properly
                break

            coo.append(Point(x * 100 + 4, rule(x) * -100 + 250))
        except ValueError:
            pass
    return list(zip(coo, coo[1:] + coo[:1]))[:-2]


def task1():
    """необхідно розробити блок-схему алгоритму та програму,
     що реалізує побудову графічних фігур: 5 кілець і 5 квадратів.
     Фігури розташовані в одному графічному вікні.
     Колір фігур однаковий. Поле між кільцями різної заливки.
     1 фігура малюється лініями, 2 вбудованими засобами.
    """

    win = GraphWin("Lab1 Task1", 500, 500)
    draw_circles(win, 20)
    draw_squares(win, 20)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


def task2():
    """
    Фігуру побудувати двома способами:
     1. В якості базових примітивів використати лінії;
     2. В якості базових примітивів використати багатокутник.
    Передбачити монохромний та кольоровий варіант із заливкою з різним кольором та різнокольоровими обмежувальними
    лініями. Кольорову гаму обрати за одним із відомих способів комбінації кольорів.
    """

    win = GraphWin("Lab1 Task2", 1000, 1000)
    radius = 120
    delta = 40

    # Colorful logo using lines
    draw_ring_using_lines(win, radius, 10, color_rgb(0, 186, 254), 250, 250 - radius + delta)  # blue
    draw_ring_using_lines(win, radius, 10, color_rgb(145, 35, 243), 250 - radius + delta, 250)  # violet
    draw_ring_using_lines(win, radius, 10, color_rgb(255, 55, 55), 250, 250 + radius - delta)  # red
    draw_ring_using_lines(win, radius, 10, color_rgb(255, 242, 0), 250 + radius - delta, 250)  # yellow

    # Monochrome logo using lines
    draw_ring_using_lines(win, radius, 10, 'black', 750, 250 - radius + delta)
    draw_ring_using_lines(win, radius, 10, 'black', 750 - radius + delta, 250)
    draw_ring_using_lines(win, radius, 10, 'black', 750, 250 + radius - delta)
    draw_ring_using_lines(win, radius, 10, 'black', 750 + radius - delta, 250)

    # Colorful logo using polygon
    draw_ring_using_polygon(win, radius, 10, color_rgb(0, 186, 254), 250, 750 - radius + delta)  # blue
    draw_ring_using_polygon(win, radius, 10, color_rgb(145, 35, 243), 250 - radius + delta, 750)  # violet
    draw_ring_using_polygon(win, radius, 10, color_rgb(255, 55, 55), 250, 750 + radius - delta)  # red
    draw_ring_using_polygon(win, radius, 10, color_rgb(255, 242, 0), 250 + radius - delta, 750)  # yellow

    # Monochrome logo using polygon
    draw_ring_using_polygon(win, radius, 10, 'black', 750, 750 - radius + delta)
    draw_ring_using_polygon(win, radius, 10, 'black', 750 - radius + delta, 750)
    draw_ring_using_polygon(win, radius, 10, 'black', 750, 750 + radius - delta)
    draw_ring_using_polygon(win, radius, 10, 'black', 750 + radius - delta, 750)

    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


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

    def draw_line(window, coordinates, color):
        for i in coordinates:
            line = Line(i[0], i[1])
            line.setOutline(color)
            line.draw(window)

    def draw_signal(rule, color):
        win = draw_axes()
        xs = get_xs(win)
        coo = get_coordinates(rule, xs)
        draw_line(win, coo, color)
        return win, coo

    win1, coo1 = draw_signal(first, 'red')
    win2, coo2 = draw_signal(second, 'green')
    win3, coo3 = draw_signal(third, 'cyan')

    win4 = draw_axes()
    draw_line(win4, coo1, 'red')
    draw_line(win4, coo2, 'green')
    draw_line(win4, coo3, 'cyan')

    win4.getMouse()  # Pause to view result
    win4.close()  # Close window when done
    win3.getMouse()  # Pause to view result
    win3.close()  # Close window when done
    win2.getMouse()  # Pause to view result
    win2.close()  # Close window when done
    win1.getMouse()  # Pause to view result
    win1.close()  # Close window when done
