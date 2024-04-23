import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class CupButton(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.width: int = 16
        self.height: int = 14
        self.col: int = 7
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
        pyxel.line(
            self.x + self.width * 1/6,
            self.y,
            self.x + self.width * 5/6,
            self.y,
            self.col
        )
        pyxel.line(
            self.x + self.width * 1/6,
            self.y,
            self.x,
            self.y + self.height,
            self.col
        )
        pyxel.line(
            self.x + self.width * 5/6,
            self.y,
            self.x + self.width,
            self.y + self.height,
            self.col
        )
