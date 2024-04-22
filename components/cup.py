import pyxel

from objects.gameobject import GameObject

class Cup(GameObject):
    def __init__(self, x: float=32, y: float=85):
        super().__init__(x, y)
        self.width = 50
        self.height = 32

    def update(self):
        pass

    def draw(self):
        pyxel.rect(
            self.x,
            self.y,
            self.width,
            self.height,
            col=7
        )
