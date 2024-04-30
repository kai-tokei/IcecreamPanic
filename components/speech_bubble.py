import pyxel
from objects.gameobject import GameObject

class SpeechBubble(GameObject):
    def __init__(self, x: float=4, y: float=3):
        super().__init__(x, y)
        self.upper: self.Sprite = self.Sprite(
            u=48, v=48, colkey=0)
        self.body: self.Sprite = self.Sprite(
            u=48, v=56, colkey=0)
        self.bottom: self.Sprite = self.Sprite(
            u=48, v=64, colkey=0)
        self.LENGTH: int = 5

    def udpate(self):
        pass

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            img=self.upper.img,
            u=self.upper.u,
            v=self.upper.v,
            w=self.upper.w,
            h=self.upper.h,
            colkey=self.upper.colkey
        )
        for y in range(1, self.LENGTH):
            pyxel.blt(
                self.x,
                self.y+(y*16),
                img=self.body.img,
                u=self.body.u,
                v=self.body.v,
                w=self.body.w,
                h=self.body.h,
                colkey=self.body.colkey
            )
        pyxel.blt(
            self.x,
            self.y+(self.LENGTH*16),
            img=self.bottom.img,
            u=self.bottom.u,
            v=self.bottom.v,
            w=self.bottom.w,
            h=self.bottom.h,
            colkey=self.bottom.colkey
        )
