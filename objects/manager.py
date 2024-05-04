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
from consts.icecreamstackitem import IceCreamStackItem

class Manager:
    def __init__(self) -> None:
        # ControllPalette
        self.iceButtons_list = self.makeIceButtons()
        self.KINDS_OF_ICE: list[int] = [i for i in range(7)]  # 登録されているアイスの種類
        self.cupButton: CupButton = CupButton(14, 157)
        self.coneButton: ConeButton = ConeButton(14, 174)
        self.spoonButton: SpoonButton = SpoonButton(31, 172)

        self.order = Order()
        self.serve = Serve(87, 128)

        self.capital: int = 100  # 資金($)
        self.scoopStack: list[IceCreamStackItem] = []  # 今作っているアイスクリームのスタック

        self.makeOrder()

    # クリックされたアイスをスタックに追加
    def scoopIce(self):
        for i in self.iceButtons_list:
            if i.isClicked():
                self.scoopStack.append(IceCreamStackItem(iceIndex=i.kind))

    # スプーンを追加
    def addSpoon(self):
        if self.spoonButton.isClicked():
            self.scoopStack.append(IceCreamStackItem(tag="spoon"))

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
        self.order.clear()
        # カップかコーンをランダムで選択
        self.order.push(IceCreamStackItem(tag= "cone" if random.randint(0, 1) else "cup"))
        # アイスを適当にスタック
        for _ in range(lengthOfOrder):
            self.order.push(IceCreamStackItem(iceIndex=random.choice(self.KINDS_OF_ICE)))
        if random.randint(0, 1):
            self.order.push(IceCreamStackItem(tag="spoon"))

    # スタックされたアイスを描画
    def drawScoopedIce(self, x: int=47, y: int=103):
        for i in range(len(self.scoopStack)-1, -1, -1):
            crtItem = self.scoopStack[i]
            if crtItem.tag == "ice":
                Ice(x, y-i*8, crtItem.iceIndex).draw()
            elif crtItem.tag == "spoon":
                SpoonButton(x, y-i*8).draw()
                pass
            else:
                if i == 0:
                    if crtItem.tag == "cup": Cup().draw()
                    elif crtItem.tag == "cone": Cone().draw()
                else:
                    # 先にアイスを乗せようとしているから、何かアクション
                    pass

    # カップをスタック
    def pushCup(self):
        self.scoopStack.append(IceCreamStackItem(tag="cup"))

    # コーンをスタック
    def pushCone(self):
        self.scoopStack.append(IceCreamStackItem(tag="cone"))

    # カップまたはコーンが押されたら、スタック
    def pushCupOrCone(self):
        # カップとコーンの追加
        if self.coneButton.isClicked(): self.pushCone()
        if self.cupButton.isClicked(): self.pushCup()

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
            if self.checkProduct():
                self.capital += 10 + len(self.scoopStack)
                self.makeOrder()
            else:
                self.capital -= (10 + len(self.scoopStack)) // 2
            self.scoopStack = []

    # 完成品がオーダーと合っているか確認
    def checkProduct(self) -> bool:
        # 長さが異なっていたら、間違い
        if len(self.scoopStack) != len(self.order.orderStack):
            return False
        # 種類を確認していく
        for i in range(len(self.scoopStack)):
            scoopTag = self.scoopStack[i].tag
            orderTag = self.order.orderStack[i].tag
            if scoopTag == orderTag:
                if scoopTag == "ice":
                    if self.scoopStack[i].iceIndex == self.order.orderStack[i].iceIndex:
                        continue
                    else:
                        return False
            else:
                return False
        return True

    def update(self):
        self.scoopIce()
        self.serve.update()
        self.serveProduct()
        self.pushCupOrCone()
        self.addSpoon()

    def draw(self):
        pyxel.cls(1)
        self.drawControllPanel()
        self.serve.draw()
        self.order.draw()
        self.drawScoopedIce()

        pyxel.text(90, 4, f'${self.capital}', 7)
