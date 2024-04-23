import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class ConeButton(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.width: int = 16
        self.height: int = 18
        self.col: int = 9
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
        pyxel.trib(
            self.x + self.width/2,
            self.y,
            self.x,
            self.y + self.height,
            self.x + self.width,
            self.y + self.height,
            self.col
        )
