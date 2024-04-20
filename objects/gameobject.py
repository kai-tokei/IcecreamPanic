import pyxel

class GameObject:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, *self.image)
