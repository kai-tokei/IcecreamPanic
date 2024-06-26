import pyxel

from objects.gameobject import GameObject

from components.button.cone_button import ConeButton
from components.button.spoon_button import SpoonButton
from components.ice import Ice
from components.cup import Cup
from components.speech_bubble import SpeechBubble

from consts.icecreamstackitem import IceCreamStackItem

class Order(GameObject):
    def __init__(self, x: float=4, y: float=125):
        super().__init__(x, y)
        self.orderStack: list[IceCreamStackItem] = []
        self.speechBubble = SpeechBubble(y=18)

    def push(self, item: IceCreamStackItem):
        self.orderStack.append(item)

    def clear(self):
        self.orderStack.clear()

    def get(self) -> list[IceCreamStackItem]:
        return self.orderStack

    def drawIce(self, x: int, y: int, kind: int):
        ice = Ice(x, y, kind)
        ice.draw()

    def drawCup(self, x: int, y: int):
        cup = Cup(x, y)
        cup.draw()

    def drawCone(self, x: int, y: int):
        cone = ConeButton(x, y)
        cone.draw()

    def drawSpoon(self, x: int, y: int):
        spoon = SpoonButton(x, y)
        spoon.draw()

    def draw(self):
        X = self.x
        for y in range(len(self.orderStack)):
            Y = self.y - 16*y
            if self.orderStack[y].tag == "cone":
                self.drawCone(X, Y)
            elif self.orderStack[y].tag == "cup":
                self.drawCup(X, Y)
            elif self.orderStack[y].tag == "spoon":
                self.drawSpoon(X, Y)
            else:
                self.drawIce(X, Y, kind=self.orderStack[y].iceIndex)
        self.speechBubble.draw()
