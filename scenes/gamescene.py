class GameScene:
    def __init__(self, font, w, h):
        self.text = font.render("Playing The Game", True, "green", "blue")
        self.textRect = self.text.get_rect()
        self.textRect.center = (w / 2, h / 2)