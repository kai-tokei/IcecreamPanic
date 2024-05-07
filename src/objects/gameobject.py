import pyxel
from objects.image import Image

class GameObject:
    class Sprite:
        def __init__(
                self,
                img: int=0,
                u: int=0,
                v: int=0,
                w: int=16,
                h: int=16,
                colkey: int=None,
            ) -> None:
            self.img = img
            self.u = u
            self.v = v
            self.w = w
            self.h = h
            self.colkey = colkey

    def __init__(
            self,
            x: float,
            y: float,
            sprite: Sprite=Sprite(),
            ):
        self.sp: self.Sprite = sprite
        self.x: float = x
        self.y: float = y

    def update(self):
        pass

    def draw(self):
        if self.sp.img >= 0:
            if self.sp.colkey == None:
                pyxel.blt(self.x, self.y, self.sp.img, self.sp.u, self.sp.v, self.sp.w, self.sp.h)
            else:
                pyxel.blt(self.x, self.y, self.sp.img, self.sp.u, self.sp.v, self.sp.w, self.sp.h, self.sp.colkey)
