import pyxel
from objects.gameobject import GameObject

class CapitalSnack(GameObject):
    def __init__(self, x: float=90, y: float=4, corrected: bool=True, point: int=10, exist: bool=True):
        super().__init__(x, y)
        self.corrected: bool = corrected
        self.point: int = point
        self.time: int = 0
        self.col: int = 3 if corrected else 8
        self.G: float = 9.8 * 0.1
        self.showTime: float = 60 * 0.5
        self.vy: float = 0
        self.exist: bool = exist

    def update(self):
        if self.y < 10:
            self.y += self.vy
            self.vy += self.G
        self.time += 1
        if self.time >= self.showTime:
            self.exist = False

    def draw(self):
        if self.exist:
            pyxel.text(self.x, self.y, f'${self.point}', col=self.col)

