import pyxel
from objects.gameobject import GameObject

class Order(GameObject):
    class OrderItem:
        def __init__(self, tag: str="ice", iceIndex: int=0) -> None:
            self.tag: str =tag
            self.iceIndex: int = iceIndex

    def __init__(self, x: float=16, y: float=25):
        super().__init__(x, y)
        self.orderStack: list[self.OrderItem] = []

    def push(self, item: OrderItem):
        pass

    def clear(self):
        pass

    def drawIce(self):
        pass

    def drawCup(self):
        pass

    def drawCone(self):
        pass

    def draw(self):
        pass
