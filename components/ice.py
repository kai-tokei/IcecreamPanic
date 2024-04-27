import pyxel
from objects.gameobject import GameObject

class Ice(GameObject):
    def __init__(self, x: float, y: float, col: int):
        super().__init__(x, y)
        self.col = col

    def draw(self):
        pyxel.circ(self.x, self.y, r=15, col=self.col)
