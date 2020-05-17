import numpy
import pygame
import random

# COLORS GUIDE
colorKey = {
    "Healthy": (0, 0, 255),  # Blue
    "Immune": (0, 255, 0),  # Green
    "Sick": (255, 0, 0),  # Red
    "Infected": (255, 150, 0),  # Orange
    "Dead": (0, 0, 0)  # Black
}


class Dot(pygame.sprite.Sprite):
    count = 0

    # Constructor
    def __init__(self, start=(0, 0), end=(0, 0), state="Healthy", size=5, SD6=True, SIP=True):
        super().__init__()
        self.position = start
        self.end = end
        self.current = start
        self.state = state
        self.size = size
        self.color = colorKey[self.state]
        self.direction = True
        self.time = 0
        self.startHold = 0
        self.endHold = 0
        self.recovery = 0
        self.SD6 = SD6
        self.SIP = SIP
        self.rect = pygame.Rect(self.position[0] - self.size, self.position[1] - self.size,
                                self.size * 2, self.size * 2)
        self.radius = size * 2

    # Move to targeted position
    def move(self):
        sx = numpy.sign(self.end[0] - self.position[0])
        nx = self.position[0] + sx
        sy = numpy.sign(self.end[1] - self.position[1])
        ny = self.position[1] + sy
        self.position = (nx, ny)
        self.rect = pygame.Rect(self.position[0] - self.size, self.position[1] - self.size,
                                self.size * 2, self.size * 2)

    # Moves Back and Forth
    def Back(self):
        if self.current == self.end:
            self.direction = False
        elif self.current == self.position:
            self.direction = True

        if self.direction:
            sx = numpy.sign(self.end[0] - self.current[0])
            nx = self.current[0] + sx
            sy = numpy.sign(self.end[1] - self.current[1])
            ny = self.current[1] + sy
        else:
            sx = numpy.sign(self.position[0] - self.current[0])
            nx = self.current[0] + sx
            sy = numpy.sign(self.position[1] - self.current[1])
            ny = self.current[1] + sy
        self.current = (nx, ny)
        self.rect.x = self.current[0]
        self.rect.y = self.current[1]

    # Determines for infection
    def hasInfection(self):
        chance = random.randint(0, 10)
        if self.state == "Immune":
            return None
        elif chance <= 8 and self.state == "Healthy":
            self.updateState("Infected")
            self.update()

    def stop(self):
        self.startHold = self.position
        self.endHold = self.end
        self.position = self.current
        self.end = self.current
        self.rect.x = self.current[0]
        self.rect.y = self.current[1]
        self.time = 0

    def time_reset(self):
        self.time = 0

    def recover(self):
        # self.position = self.startHold
        # self.end = self.endHold
        chance = random.randint(0, 100)
        if chance <= 98:
            self.updateState("Immune")
            if self.SD6 == True:
                self.position = self.startHold
                self.end = self.endHold
            else:
                self.position = self.position
                self.end = self.end
        else:
            self.updateState("Dead")
            self.position = self.current
            self.end = self.current

    # Fix Avoid method two different methods?
    def avoid(self):
        # print("Original1:", self.current, (self.rect.x, self.rect.y))
        if self.SIP == False and self.state in ("Healhty","Infected","Immune"):
            self.current = (self.current[0] * 1.1, self.current[1] * 1.1)
            self.rect.x = self.current[0]
            self.rect.y = self.current[1]
            self.update()
        # print("After Collision1: ", self.current, (self.rect.x, self.rect.y))

    def avoid2(self):
        # print("Original2:", self.current, (self.rect.x, self.rect.y))
        if self.SIP == False and self.state in ("Healhty","Infected","Immune"):
            self.current = (self.current[0] * .9, self.current[1] * .9)
            self.rect.x = self.current[0]
            self.rect.y = self.current[1]
            self.update()
        # print("After Collision2: ", self.current, (self.rect.x, self.rect.y))

    # A single method maybe?
    def avoid3(self):
        if self.current[0] < 500 and self.current[1] < 500:
            self.current = (self.current[0] + self.size, self.current[1] + self.size)
        elif self.current[0] > 500 and self.current[1] > 500:
            self.current = (self.current[0] - self.size, self.current[1] - self.size)

    def isInfected(self):
        if self.state == "Sick" or self.state == "Infected":
            return True
        else:
            return False

    # updates state of dot
    def updateState(self, state):
        self.state = state
        self.color = colorKey[self.state]

'''
NOTES:
Collision Avoidance works to a certain extent, but after a few collisions it begins to create
a stasis for some of the dots not allowing them to move. To test it out remove the '#' from
i.avoid() and j.avoid2() in my 'for j in hit_list:' loop in the scenarios.
'''

