import pyxel
from objects.image import Image

class GameObject:
    def __init__(self, x: float, y: float, image: Image):
        self.x: float = x
        self.y: float = y
        self.image: Image = image

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, *self.image)
