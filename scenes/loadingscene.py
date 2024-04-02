from scenes.scene import Scene

class LoadingScene(Scene):

    def __init__(self, font, w, h):
        super().__init__(font, w, h, "Starting Up . . please wait")
        self.counter=500

    def draw(self, screen, dt):
        Scene.draw(self, screen, dt)
        self.counter-=1

    
    def transition(self):
        return (self.counter <= 0)