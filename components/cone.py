import pyxel

from objects.gameobject import GameObject

class Cone(GameObject):
    def __init__(self, x: float=34, y: float=90):
        super().__init__(x, y)
        self.img = 0
        self.u = 0
        self.v = 16
        self.w = 16
        self.h = 32
        self.colkey = 0

    def update(self):
        pass

    def draw(self):
        return super().draw()
    '''
    def draw(self):
        pyxel.tri(
            self.x,
            self.y,
            self.x + self.w,
            self.y,
            self.x + self.w/2,
            self.y + self.h,
            col=9
        )
    '''
