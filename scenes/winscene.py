from scenes.scene import Scene

class WinScene(Scene):

    def __init__(self, font, w, h):
        super().__init__(font, w, h, "Player X Won!!!")
