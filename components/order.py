import pyxel
from objects.gameobject import GameObject

class Order(GameObject):
    def __init__(self, x: float=16, y: float=25):
        super().__init__(x, y)
        self.orderStack: list[int] = []
        self.cupORcone: str = ""

    def update(self, orderStack: list[int], cupORcone):
        self.orderStack = orderStack
        self.cupORcone = cupORcone

    def draw(self):
        if self.cupORcone == "cup":
            pyxel.circb(self.x, 28, 5, 0)
        else:
            pyxel.circb(self.x, 28, 5, 9)

        for i in range(len(self.orderStack)):
            pyxel.circ(self.x, 25-i*5, 5, self.orderStack[i])
