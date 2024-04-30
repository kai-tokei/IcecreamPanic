import pyxel
from objects.gameobject import GameObject

class Ice(GameObject):
    def __init__(self, x: float, y: float, kind: int=0):
        super().__init__(x, y)
        self.kind = kind
        self.sp = self.Sprite(
            u=16+kind%3*16, v=(kind//3)*16, colkey=0)

    def draw(self):
        return super().draw()
