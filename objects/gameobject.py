import pyxel
from objects.image import Image

class GameObject:
    def __init__(
            self,
            x: float,
            y: float,
            img: int=-1,
            u: int=0,
            v: int=5,
            w: int=5,
            h: int=5,
            colkey: int=None,
            ):
        self.x: float = x
        self.y: float = y
        self.img = img
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey

    def update(self):
        pass

    def draw(self):
        if self.img > 0:
            if self.colkey == None:
                pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h)
            else:
                pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, self.colkey)
