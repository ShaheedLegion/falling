import pygame
from scenes.loadingscene import LoadingScene
from scenes.playerwaitscene import PlayerWaitScene
from scenes.gamescene import GameScene
from scenes.winscene import WinScene

from starsbg import StarsBackground

class SceneManager:

    def __init__(self, numStars, numLayers, w, h):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.scenes = [
            LoadingScene(self.font, w, h),
            PlayerWaitScene(self.font, w, h),
            GameScene(self.font, w, h),
            WinScene(self.font, w, h),
        ]
        self.currentScene = 0
        self.stars = StarsBackground(numStars, numLayers, w, h)

    def draw(self, screen, dt):
        self.stars.draw(screen, dt) # first draw the background
        self.scenes[self.currentScene].draw(screen, dt)

        if self.scenes[self.currentScene].transition():
            match self.currentScene:
                case 0:
                    self.currentScene = 1
                case 1:
                    self.currentScene = 2
                case 2:
                    self.currentScene = 3
                case 3:
                    self.currentScene = 1
