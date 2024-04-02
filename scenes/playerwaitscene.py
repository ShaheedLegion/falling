from scenes.scene import Scene

class PlayerWaitScene(Scene):
    def __init__(self, font, w, h):
        super().__init__(font, w, h, "Waiting for Player 2")
