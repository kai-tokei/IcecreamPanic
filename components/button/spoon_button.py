import pyxel

from objects.gameobject import GameObject
from objects.button import Button

class SpoonButton(GameObject):
    def __init__(self, x: float, y: float, sprite: GameObject.Sprite = GameObject.Sprite(
        u=32, v=48, colkey=0
    )):
        super().__init__(x, y, sprite)
        self.button = Button(
            x, y, 16, 16)

    def update(self):
        pass

    def draw(self):
        return super().draw()


