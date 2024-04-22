import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class IceButton(GameObject):
    def __init__(self, x: float, y: float, col: int = 0):
        super().__init__(x, y)
        self.width: int = 16
        self.height: int = 18
        self.col: int = col
        self.button: Button = Button(
            self.x,
            self.y,
            width=self.width,
            height=self.height)
        self.clicked = False

    def calIsClicked(self):
        return self.button.isClicked(
            pyxel.MOUSE_POS_X, pyxel.MOUSE_POS_Y)

    def isClicked(self):
        return self.clicked

    def update(self):
        self.calIsClicked()

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.col)
