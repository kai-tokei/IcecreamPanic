import pyxel
from objects.gameobject import GameObject

class IceButton(GameObject):
    def __init__(self, x: float, y: float, col: int = 0):
        super().__init__(x, y)
        self.width: int = 16
        self.height: int = 18
        self.col: int = col

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.col)
