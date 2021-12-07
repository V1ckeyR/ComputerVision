import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from lab7.figures.cylinder import draw_cylinder
from lab7.figures.pyramid import draw_pyramid

if __name__ == "__main__":
    pygame.init()
    display = (800, 600)
    pygame.display.set_caption("Lab 7")
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -15)

    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 1, 1))  # point light from the left, top, front
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_LEFT]:
            glRotatef(5, 0, 0, 1)
        if keys[pygame.K_RIGHT]:
            glRotatef(5, 0, 0, -1)
        if keys[pygame.K_UP]:
            glRotatef(5, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(5, -1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

        draw_pyramid(2, (-5, 0))
        draw_cylinder(1, 4, 20, (5, 0))

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)
