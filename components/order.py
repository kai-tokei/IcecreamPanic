import pyxel

from objects.gameobject import GameObject

from components.button.cone_button import ConeButton
from components.ice import Ice
from components.cup import Cup
from components.speech_bubble import SpeechBubble

class Order(GameObject):
    class OrderItem:
        def __init__(self, tag: str="ice", iceIndex: int=0, pos: str="center") -> None:
            self.tag: str =tag
            self.iceIndex: int = iceIndex
            self.pos: str = pos

    def __init__(self, x: float=16, y: float=25):
        super().__init__(x, y)
        self.orderStack: list[self.OrderItem] = []
        self.speechBubble = SpeechBubble()

    def push(self, item: OrderItem):
        self.orderStack.append(item)

    def clear(self):
        self.orderStack.clear()

    def drawIce(self, x: int, y: int, kind: int):
        ice = Ice(x, y, kind)
        ice.draw()

    def drawCup(self, x: int, y: int):
        cup = Cup(x, y)
        cup.draw()

    def drawCone(self, x: int, y: int):
        cone = ConeButton(x, y)
        cone.draw()

    def draw(self):
        self.speechBubble.draw()
