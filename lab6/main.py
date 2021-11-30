from lab6.pyramid.generator import draw_pyramids
from lab6.pyramid.fractals import *


def background(w):
    lake(w)
    mountains(w)


if __name__ == '__main__':
    win = GraphWin("Lab6", 600, 500)
    win.setBackground('black')
    background(win)
    draw_pyramids(win, background)
