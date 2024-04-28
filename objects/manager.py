import pyxel
import random

# Components
from components.button.cone_button import ConeButton
from components.button.cup_button import CupButton
from components.button.ice_button import IceButton
from components.cone import Cone
from components.cup import Cup
from components.speech_bubble import SpeechBubble
from components.serve import Serve
from components.ice import Ice
from components.order import Order

# consts

class Manager:
    def __init__(self) -> None:
        # ControllPalette
        self.iceButtons_list = [
            IceButton(31, 146, 3),
            IceButton(50, 146, 7),
            IceButton(69, 146, 8),
            IceButton(88, 146, 9),

            IceButton(31, 167, 10),
            IceButton(50, 167, 11),
            IceButton(69, 167, 14),
            IceButton(88, 167, 15),
        ]
        self.KIND_OF_ICE: list[int] = [3, 7, 8, 9, 10, 11, 14, 15]  # 登録されているアイスの種類
        self.cupButton: CupButton = CupButton(8, 146)
        self.coneButton: ConeButton = ConeButton(8, 167)

        self.speech = SpeechBubble()
        self.order = Order()
        self.serve = Serve()

        self.capital: int = 100  # 資金($)
        self.cupORcone: str = ""
        self.ordercupORcone: str = ""
        self.scoopStack: list[any] = []  # 今作っているアイスクリームのスタック
        self.orderStack: list[any] = []  # 注文されたアイスクリームのスタック

    # クリックされたアイスをスタックに追加
    def scoopIce(self):
        for i in self.iceButtons_list:
            if i.isClicked():
                self.scoopStack.append(i.col)

    # 注文を生成
    def makeOrder(self):
        lengthOfOrder: int = random.randint(1, 6)
        order: list[int] = []
        for i in range(lengthOfOrder):
            order.append(random.choice(self.KIND_OF_ICE))
        self.ordercupORcone = "cup" if random.randint(0, 1) else "cone"
        self.orderStack = order

    # スタックされたアイスを描画
    def drawScoopedIce(self):
        for i in range(len(self.scoopStack)):
            Ice(50, 90-i*15, self.scoopStack[i]).draw()

    # カップかコーンを描画
    def drawCupORCone(self):
        if self.cupORcone == "cup":
            Cup().draw()
        elif self.cupORcone == "cone":
            Cone().draw()

    # カップまたはコーンが押されたら、指定
    def addCupORCone(self):
        if self.cupButton.isClicked():
            self.cupORcone = "cup"
        elif self.coneButton.isClicked():
            self.cupORcone = "cone"

    # アイスクリームのボタンを描画
    def drawIcecreamButtons(self):
        [i.draw() for i in self.iceButtons_list]

    # コントロールパネルを描画
    def drawControllPanel(self):
        self.cupButton.draw()
        self.coneButton.draw()
        self.drawIcecreamButtons()

    # アイスクリームを給仕
    def serveProduct(self):
        if self.serve.isClicked():
            self.makeOrder()
            self.scoopStack = []
            self.cupORcone = ""

    def update(self):
        self.scoopIce()
        self.serve.update()
        self.addCupORCone()
        self.order.update(self.orderStack, self.ordercupORcone)
        self.serveProduct()

    def draw(self):
        pyxel.cls(0)
        self.drawControllPanel()
        self.speech.draw()
        self.serve.draw()
        self.drawScoopedIce()
        self.drawCupORCone()
        self.order.draw()

        pyxel.text(90, 4, "$100", 7)
