import pyxel

from objects.gameobject import GameObject

class Cone(GameObject):
    def __init__(self, x: float=34, y: float=90):
        super().__init__(
            x,
            y,
            self.Sprite(
                img=0, u=0, v=16, w=16, h=32, colkey=0
            )
        )


    def update(self):
        pass

    def draw(self):
        return super().draw()
