import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class ConeButton(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(
            x,
            y,
            self.Sprite(
                u=0, v=0, colkey=0
            )
        )
        self.width: int = 16
        self.height: int = 16
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
        return super().draw()
