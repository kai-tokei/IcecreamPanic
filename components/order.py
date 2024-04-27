import pyxel
from objects.gameobject import GameObject

class Order(GameObject):
    def __init__(self, x: float=16, y: float=25):
        super().__init__(x, y)
        self.orderStack: list[int] = []

    def update(self, orderStack: list[int]):
        self.orderStack = orderStack

    def draw(self):
        for i in range(len(self.orderStack)):
            pyxel.circ(self.x, 25-i*5, 5, self.orderStack[i])
