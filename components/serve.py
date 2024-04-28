import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class Serve(GameObject):
    def __init__(self, x: float=90, y: float=125):
        super().__init__(x, y)
        self.x: int = x
        self.y: int = y
        self.r: int = 12
        self.col: int = 3
        self.button: Button = Button(self.x - self.r, self.y - self.r, self.r*2, self.r*2)

    def isClicked(self) -> bool:
        return self.button.isClicked()

    def update(self):
        if self.button.isInside(pyxel.MOUSE_POS_X, pyxel.MOUSE_POS_Y):
            self.col = 4
        else:
            self.col = 3

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.col)
