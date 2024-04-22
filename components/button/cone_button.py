import pyxel
from objects.gameobject import GameObject

class ConeButton(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.width: int = 16
        self.height: int = 18
        self.col: int = 9

    def draw(self):
        pyxel.trib(
            self.x + self.width/2,
            self.y,
            self.x,
            self.y + self.height,
            self.x + self.width,
            self.y + self.height,
            self.col
        )
