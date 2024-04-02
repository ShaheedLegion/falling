from scenes.scene import Scene

class GameScene(Scene):

    def __init__(self, font, w, h):
        super().__init__(font, w, h, "Playing The Game")
