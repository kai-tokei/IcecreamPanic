import pyxel

from objects.gameobject import GameObject

class Cone(GameObject):
    def __init__(self, x: float=34, y: float=90):
        super().__init__(x, y)
        self.width = 32
        self.height = 50

    def update(self):
        pass

    def draw(self):
        pyxel.tri(
            self.x,
            self.y,
            self.x + self.width,
            self.y,
            self.x + self.width/2,
            self.y + self.height,
            col=9
        )
