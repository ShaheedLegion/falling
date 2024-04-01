import pygame
import random

class Star:
    def __init__(self, w, h, numLayers):
        self.pos = pygame.Vector2(random.randint(0, w) , random.randint(0, h))
        self.layer = random.randint(0, numLayers-1)
        self.color = pygame.Color(128 + (random.randint(0, 64)) + (20 * self.layer),
        24 + (24 * self.layer), 96 + (random.randint(0, 64)) + (26 * self.layer))