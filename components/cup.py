import pyxel

from objects.gameobject import GameObject

class Cup(GameObject):
    def __init__(self, x: float=32, y: float=90):
        super().__init__(
            x,
            y,
            self.Sprite(
                u=0, v=48, colkey=0)
        )

    def update(self):
        pass

    def draw(self):
        return super().draw()
