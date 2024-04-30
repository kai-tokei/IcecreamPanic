import pyxel
import random

# Components
from components.button.cone_button import ConeButton
from components.button.cup_button import CupButton
from components.button.ice_button import IceButton
from components.button.spoon_button import SpoonButton
from components.cone import Cone
from components.cup import Cup
from components.serve import Serve
from components.ice import Ice
from components.order import Order

# consts

class Manager:
    def __init__(self) -> None:
        # ControllPalette
        self.iceButtons_list = self.makeIceButtons()
        self.KINDS_OF_ICE: list[int] = [i for i in range(8)]  # 登録されているアイスの種類
        self.cupButton: CupButton = CupButton(14, 157)
        self.coneButton: ConeButton = ConeButton(14, 174)
        self.spoonButton: SpoonButton = SpoonButton(31, 172)

        self.order = Order()
        self.serve = Serve(87, 128)

        self.capital: int = 100  # 資金($)
        self.scoopStack: list[any] = []  # 今作っているアイスクリームのスタック
        self.orderStack: list[any] = []  # 注文されたアイスクリームのスタック

    # クリックされたアイスをスタックに追加
    def scoopIce(self):
        for i in self.iceButtons_list:
            if i.isClicked():
                self.scoopStack.append(i.kind)

    # アイスのボタンを生成
    def makeIceButtons(self) -> list[IceButton]:
        iceButtons_list = []
        for i in range(7):
            iceButtons_list.append(IceButton(
                x=31+(i//4*16)+(i%4)*16, y=156+i//4*16, kind=i))
        return iceButtons_list

    # 注文を生成
    def makeOrder(self):
        lengthOfOrder: int = random.randint(1, 6)
        order: list[int] = []
        for i in range(lengthOfOrder):
            order.append(random.choice(self.KINDS_OF_ICE))
        self.orderStack = order

    # スタックされたアイスを描画
    def drawScoopedIce(self, x: int=47, y: int=95):
        for i in range(len(self.scoopStack)):
            Ice(x, y-i*8, self.scoopStack[i]).draw()

    # カップまたはコーンが押されたら、スタック
    def pushCupORCone(self):
        if self.cupButton.isClicked():
            pass
        elif self.coneButton.isClicked():
            pass

    # アイスクリームのボタンを描画
    def drawIcecreamButtons(self):
        [i.draw() for i in self.iceButtons_list]

    # コントロールパネルを描画
    def drawControllPanel(self):
        pyxel.rect(0, 152, 108, 40, col=7)
        self.cupButton.draw()
        self.coneButton.draw()
        self.spoonButton.draw()
        self.drawIcecreamButtons()

    # アイスクリームを給仕
    def serveProduct(self):
        if self.serve.isClicked():
            self.scoopStack = []

    def update(self):
        self.scoopIce()
        self.serve.update()
        self.pushCupORCone()
        self.serveProduct()
        self.spoonButton.update()

    def draw(self):
        pyxel.cls(1)
        self.drawControllPanel()
        self.serve.draw()
        self.order.draw()
        self.drawScoopedIce()

        pyxel.text(90, 4, "$100", 7)
