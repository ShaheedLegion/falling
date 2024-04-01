import pygame
import random
from star import Star

class StarsBackground:

    def __init__(self, numStars, numLayers, sw, sh):
        self.numStars = numStars
        self.numLayers = numLayers
        self.screenWidth = sw
        self.screenHeight = sh
        self.stars = [ self.generate_star(i) for i in range(self.numStars) ]

    def generate_star(self, i):
        return Star(self.screenWidth, self.screenHeight, self.numLayers)

    def draw(self, screen, dt):
        for i in range(self.numStars):
            layer = self.stars[i].layer
            pygame.draw.circle(screen, self.stars[i].color, self.stars[i].pos, (1 + layer) / 2)
            self.stars[i].pos.y += (5 * dt) + (layer * dt * 10)

            if self.stars[i].pos.y > self.screenHeight:
                self.stars[i].pos.y = 0
