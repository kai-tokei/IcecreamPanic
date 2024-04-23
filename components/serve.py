import pyxel
from objects.gameobject import GameObject
from objects.button import Button

class Serve(GameObject):
    def __init__(self, x: float=90, y: float=125):
        super().__init__(x, y)
        self.x: int = x
        self.y: int = y
        self.r: int = 12
        self.button: Button = Button(self.x, self.y, self.r, self.r)

    def update(self):
        self.button.isClicked()

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, 3)
