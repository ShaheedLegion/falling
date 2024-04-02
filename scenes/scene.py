class Scene:
    def __init__(self, font, w, h, string):
        self.text = font.render(string, True, "green", "blue")
        self.textRect = self.text.get_rect()
        self.textRect.center = (w / 2, h / 2)

    def draw(self, screen, dt):
        screen.blit(self.text, self.textRect)
    
    def transition(self):
        return False
