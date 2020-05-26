import random
from OpenGL.GL import *
import math
import pygame
from math import *

pygame.mixer.init()
explosion = pygame.mixer.Sound('explosion-01.wav')
fuse = pygame.mixer.Sound('bomb-fuse-wick-burning-01.wav')


class Particle:
    def __init__(self, x=0, y=0, z=0, color=(0, 0, 0, 1), trail=10, secondary=False):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.exploded = False
        self.pop = 0
        self.lifetime = random.randrange(150, 300, 1)
        self.length = trail
        self.velocity = [random.uniform(-.01, .01), random.uniform(-.01, .01), random.uniform(-.01, .01), ]
        self.acceleration = 0.001
        self.counter = 0
        self.queue = []
        self.dt = .1
        self.second = secondary
        self.newExplosion = Firework()
        self.recursion = 1

    def update(self):
        self.color = list(self.color)
        deltaT = self.dt * self.counter
        theta = degrees(atan2(self.y, self.x))
        if self.y > 10:
            self.exploded = True
            self.pop += 1
        # Creates explosion sound
        if self.pop == 1:
            fuse.stop()
            explosion.play()
        if self.exploded:
            # Projectile motion of firework
            self.x += self.velocity[0] * deltaT
            self.y += self.velocity[1] * deltaT - (.5 * self.acceleration * math.pow(deltaT, 2))
            self.z += self.velocity[2] * deltaT
            # Change alpha for particles
            r, g, b, a = self.color
            transparency = 1 - (self.counter / self.lifetime)
            self.color = (r, g, b, transparency)
            # Comet trail queue
            if len(self.queue) < self.length:
                self.queue.append((self.x, self.y, self.z))
            else:
                self.queue.append((self.x, self.y, self.z))
                self.queue.pop(0)
            self.counter += 1
        else:
            # Spiral trajectory, for straight trajectory delete self.x and self.z
            self.y += .1
            self.x = theta * cos(theta) / 100
            self.z += (theta * sin(theta) / 350)
            # Plays fuse sound effect
            fuse.play()


class Firework(Particle):
    def __init__(self, n=0, position=(0, 0, 0), color=(0, 0, 0, 1)):
        self.numParticles = n
        self.color = color
        self.position = position
        self.plist = []
        for i in range(n):
            x, y, z = self.position
            pobj = Particle(x, y, z, color, 5)
            self.plist.append(pobj)

    def render(self):
        # Draws the Firework animations
        glEnable(GL_POINT_SMOOTH)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glPointSize(3)
        glBegin(GL_POINTS)
        for p in self.plist:
            glColor4fv(p.color)
            glVertex3fv((p.x, p.y, p.z))
            # Draws the comet trail
            for points in p.queue:
                glColor4fv(p.color)
                glVertex3fv(points)
            p.update()
        glEnd()