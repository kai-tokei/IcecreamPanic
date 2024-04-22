import pyxel
from objects.image import Image

class GameObject:
    def __init__(
            self,
            x: float,
            y: float):
        self.x: float = x
        self.y: float = y

    def update(self):
        pass

    def draw(self):
        pass
