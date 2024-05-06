import pyxel
import random

class Title:
    def __init__(self) -> None:
        self.text: int = 0
        self.image: int = 0

    def update(self) -> bool:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return True
        else:
            return False

    def draw(self):
        self.text += random.randint(1, 5)
        self.image += random.randint(1, 5)

        pyxel.cls(1)
        if self.text < 149:
            pyxel.blt(0, 20, 1, 0, 24, 107, 50)
        elif self.text > 150:
            self.text = 0

        if self.image < 149:
            pyxel.blt(16, 74, 1, 16, 72, 95, 143)
        elif self.image > 150:
            self.image = 0
