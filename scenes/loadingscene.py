class LoadingScene:
    def __init__(self, font, w, h):
        self.text = font.render("Starting Up . . please wait", True, "green", "blue")
        self.textRect = self.text.get_rect()
        self.textRect.center = (w / 2, h / 2)

    def draw(self, screen, dt):
        #i = 0
        screen.blit(self.text, self.textRect)
