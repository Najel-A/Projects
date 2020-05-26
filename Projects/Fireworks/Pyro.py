import random
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from Firework import Firework


def terrain():
    ''' Draws a simple square as the terrain '''
    glBegin(GL_QUADS)
    glColor4fv((0, 0, 1, 1))  # Colors are now: RGBA, A = alpha for opacity
    glVertex3fv((10, 0, 10))  # These are the xyz coords of 4 corners of flat terrain.
    glVertex3fv((-10, 0, 10))  # If you want to be fancy, you can replace this method
    glVertex3fv((-10, 0, -10))  # to draw the terrain from your prog1 instead.
    glVertex3fv((10, 0, -10))
    glEnd()


def main():
    pygame.init()

    # Set up the screen
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Firework Simulation")
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, -5, -25)

    play = True
    sim_time = 0

    # A clock object for keeping track of fps
    clock = pygame.time.Clock()

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(-10, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(10, 0, 1, 0)

                if event.key == pygame.K_UP:
                    glRotatef(-10, 1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(10, 1, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)

                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        glRotatef(0.10, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        terrain()

        # Renders firework objects
        if 0 < sim_time <= 1000:
            f1.render()

        if 500 < sim_time <= 1500:
            f2.render()
            f3.render()

        if 1000 < sim_time <= 1500:
            f4.render()
            f5.render()

        if 1500 < sim_time:
            sim_time = 0

        if sim_time == 0:
            # n creates amount of particles per Firework Object
            n = 100
            f1 = Firework(n, (0, 0, 0), (random.random(), random.random(), random.random(), 1))
            f2 = Firework(n, (-5, 0, 5), (random.random(), random.random(), random.random(), 1))
            f3 = Firework(n, (-5, 0, -5), (random.random(), random.random(), random.random(), 1))
            f4 = Firework(n, (5, 0, -5), (random.random(), random.random(), random.random(), 1))
            f5 = Firework(n, (5, 0, 5), (random.random(), random.random(), random.random(), 1))

        pygame.display.flip()
        sim_time += 1
        clock.tick(150)

    pygame.quit()


if __name__ == "__main__":
    main()
