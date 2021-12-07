from OpenGL.GL import *

colors = (
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
)

edges = (
    (0, 1), (0, 2), (0, 3),
    (1, 2), (1, 3), (2, 3)
)

surfaces = (
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
)

normals = (
    (-1, 1, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 1)
)


def draw_pyramid(s, move):
    dx, dy = move
    vertices = (
        (dx,     dy,     0),
        (dx + s, dy,     1),
        (dx,     dy + s, 1),
        (dx,     dy,     s),
    )

    glBegin(GL_TRIANGLES)
    for i_surface, surface in enumerate(surfaces):
        x = 0
        glNormal3fv(normals[i_surface])
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv(colors[0])
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
