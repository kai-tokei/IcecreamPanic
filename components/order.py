import pyxel

from objects.gameobject import GameObject
from components.ice import Ice
from components.button.cone_button import ConeButton
from components.button.cup_button import CupButton

class Order(GameObject):
    class OrderItem:
        def __init__(self, tag: str="ice", iceIndex: int=0, pos: str="center") -> None:
            self.tag: str =tag
            self.iceIndex: int = iceIndex
            self.pos: str = pos

    def __init__(self, x: float=16, y: float=25):
        super().__init__(x, y)
        self.orderStack: list[self.OrderItem] = []

    def push(self, item: OrderItem):
        self.orderStack.append(item)

    def clear(self):
        self.orderStack.clear()

    def drawIce(self, x: int, y: int):
        pass

    def drawCup(self, x: int, y: int):
        pass

    def drawCone(self, x: int, y: int):
        pass

    def draw(self):
        pass
