import math

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

from lab1.libs.CircleAngles import CircleAngles


COLORS = {
    'violet': '#9123F3',
    'blue': '#00BAFF',
    'yellow': '#FFF200',
    'red': '#FF3737',
    'green': '#00FF00',
    'white': '#FFFFFF'
}

COLORS_LIST = list(COLORS.values())
ANGELS_FOR_CIRCLE = list(CircleAngles())


def circles(ax, radius):
    for n in range(4, -1, -1):
        width = n * 10
        color = COLORS_LIST[n]

        for a in ANGELS_FOR_CIRCLE:
            x = (radius + width) * math.cos(a)
            y = (radius + width) * math.sin(a)
            ax.plot([0, x], [0, y], color)


def squares(ax, size):
    for n in range(4, -1, -1):
        color = COLORS_LIST[n]
        k = 0.08
        ax.add_patch(Rectangle((0.25-n*k/2, 0.25-n*k/2), width=size+n*k, height=size+n*k, color=color))


def task1():
    """необхідно розробити блок-схему алгоритму та програму,
     що реалізує побудову графічних фігур: 5 кілець і 5 квадратів.
     Фігури розташовані в одному графічному вікні.
     Колір фігур однаковий. Поле між кільцями різної заливки.
     1 фігура малюється лініями, 2 вбудованими засобами.
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle('Task1')

    circles(axs[0], 60)
    squares(axs[1], 0.5)

    plt.show()


def draw_figure_using_lines(ax, radius, width, *, dx, colorful):
    b, c = 1, -1
    for n in range(4):
        k = n % 3
        kx = k if k != 2 else -1
        ky = k * b + c if k != 2 else -1 * b - c

        b *= -1
        c *= -1

        color = COLORS_LIST[n] if colorful else 'k'
        for a in ANGELS_FOR_CIRCLE:
            x1 = radius * math.cos(a) + kx * dx
            y1 = radius * math.sin(a) + ky * dx
            x2 = (radius - width) * math.cos(a) + kx * dx
            y2 = (radius - width) * math.sin(a) + ky * dx

            ax.plot([x1, x2], [y1, y2], color)


def draw_figure_using_polygons(ax, radius, width, *, dx, colorful):
    b, c = 1, -1
    for n in range(4):
        x_points = []
        y_points = []

        k = n % 3
        kx = k if k != 2 else -1
        ky = k * b + c if k != 2 else -1 * b - c

        b *= -1
        c *= -1

        color = COLORS_LIST[n] if colorful else 'k'
        for a in ANGELS_FOR_CIRCLE:
            x_points.append(radius * math.cos(a) + kx * dx)
            y_points.append(radius * math.sin(a) + ky * dx)

        ax.plot(x_points, y_points, color, linewidth=width)


def task2():
    """
    Фігуру побудувати двома способами:
    1. В якості базових примітивів використати лінії;
    2. В якості базових примітивів використати багатокутник.
    Передбачити монохромний та кольоровий варіант із заливкою з різним кольором та різнокольоровими обмежувальними
    лініями. Кольорову гаму обрати за одним із відомих способів комбінації кольорів.
    """
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle('Task2')

    draw_figure_using_lines(axs[0, 0], 60, 5, dx=40, colorful=True)
    draw_figure_using_lines(axs[1, 0], 60, 5, dx=40, colorful=False)
    draw_figure_using_polygons(axs[0, 1], 60, 5, dx=40, colorful=True)
    draw_figure_using_polygons(axs[1, 1], 60, 5, dx=40, colorful=False)

    plt.show()


def draw_graphic(ax, rule, color):
    x = 0
    x_points = []
    y_points = []

    while True:
        try:
            y_points.append(rule(x))
            x_points.append(x)
        except ValueError:
            break

        x += 0.01
        if x > 1:
            break

    ax.plot(0, -max(y_points))
    ax.plot(x_points, y_points, color)


def task3():
    """
    скрипт, що реалізує побудову та відображення трьох окремих графіків епюрів тестових сигналів та четвертий графік з
    сумісним відображенням епюрів усіх трьох сигналів
    Центр координатної сітки розташований в центрі лівої межі графічного вікна. Координатні осі позначені надписами.
    Графіки різних сигналів мають різний колір.
    """
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle('Task3')

    a = 17

    def first(x): return math.acos(x)

    def second(x): return a * 0.01 * math.atan(x)

    def third(x): return a * 0.01 * math.asin(x)

    draw_graphic(axs[0, 0], first, COLORS['red'])
    draw_graphic(axs[0, 1], second, COLORS['green'])
    draw_graphic(axs[1, 0], third, COLORS['blue'])

    draw_graphic(axs[1, 1], first, COLORS['red'])
    draw_graphic(axs[1, 1], second, COLORS['green'])
    draw_graphic(axs[1, 1], third, COLORS['blue'])
    plt.show()
