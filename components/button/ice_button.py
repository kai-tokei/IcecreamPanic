import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class IceButton(GameObject):
    # kind: スプライトシート上のアイスを3x3のグリッドと捉え、左上から0~8でidを指定
    def __init__(self, x: float, y: float, kind: int = 0):
        super().__init__(x, y)
        self.width: int = 16
        self.height: int = 16
        self.kind: int = kind
        self.cover: self.Sprite = self.Sprite(
            u=16, v=48, colkey=2)
        self.ice: self.Sprite = self.Sprite(
            u=16+kind%3*16, v=16*kind//3, colkey=0)  # スプライトシート上の座標を計算して、アイスを割り当てる
        self.button: Button = Button(
            self.x,
            self.y,
            width=self.width,
            height=self.height)

    def isClicked(self):
        return self.button.isClicked()

    def update(self):
        self.isClicked()

    def draw(self):
        pyxel.blt(
            img=self.cover.img,
            u=self.cover.u,
            v=self.cover.v,
            w=self.cover.w,
            h=self.cover.h,
            colkey=self.cover.colkey)
        pyxel.blt(
            img=self.ice.img,
            u=self.ice.u,
            v=self.ice.v,
            w=self.ice.w,
            h=self.ice.h,
            colkey=self.ice.colkey)
