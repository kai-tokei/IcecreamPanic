import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class IceButton(GameObject):
    def __init__(self, x: float, y: float, col: int = 0):
        super().__init__(x, y)
        self.width: int = 16
        self.height: int = 16
        self.col: int = col
        self.cover: self.Sprite = self.Sprite(
            img=0, u=16, v=48, w=16, h=16, colkey=2
        )
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
        pyxel.rect(self.x, self.y, self.width, self.height, self.col)
