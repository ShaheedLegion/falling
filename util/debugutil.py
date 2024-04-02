import pygame

class DebugUtil:
    def __init__(self, w, h, framerate):
        self.framerate = framerate
        self.orect = pygame.Rect(0, 0, 20, self.framerate+2)
        self.irect = pygame.Rect(1, 1, 18, self.framerate-2)

    def draw(self, screen, fps):
        self.irect.update(1, 1, 18, fps)
        pygame.draw.rect(screen, "blue", self.orect, 2)
        pygame.draw.rect(screen, "green", self.irect)