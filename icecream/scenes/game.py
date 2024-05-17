import pyxel
import random
from enum import Enum, auto

# Button
from components.button.cone_button import ConeButton
from components.button.cup_button import CupButton
from components.button.ice_button import IceButton
from components.button.spoon_button import SpoonButton

# components
from components.cone import Cone
from components.cup import Cup
from components.serve import Serve
from components.ice import Ice
from components.order import Order
from components.capital_snack import CapitalSnack

# consts
from consts.icecreamstackitem import IceCreamStackItem

# ゲームの状態遷移
class GameState(Enum):
    TAP_TO_START = auto()
    GAME = auto()
    FINISHED = auto()
    TRANS_TO_SCORE = auto()

# ゲームシーン
class Game:
    def __init__(self) -> None:
        # ControllPalette
        self.iceButtons_list = self.makeIceButtons()
        self.KINDS_OF_ICE: list[int] = [i for i in range(7)]  # 登録されているアイスの種類
        self.cupButton: CupButton = CupButton(14, 157)
        self.coneButton: ConeButton = ConeButton(14, 174)
        self.spoonButton: SpoonButton = SpoonButton(31, 172)

        self.order = Order()
        self.serve = Serve(87, 128)

        self.capital: int = 0  # 資金($)
        self.capitalSnack: CapitalSnack = CapitalSnack(exist=False)

        self.scoopStack: list[IceCreamStackItem] = []  # 今作っているアイスクリームのスタック
        self.topIcePos: list[float] = [47, 0]
        self.G: float = 9.8 * 0.05
        self.vy: float = 0
        self.makeOrder()

        self.gameState: GameState = GameState.TAP_TO_START
        self.startTime: int = 0
        self.LIMIT_TIME: int = 60 * 60

        self.finished: bool = False

    # クリックされたアイスをスタックに追加
    def scoopIce(self):
        for i in self.iceButtons_list:
            if i.isClicked():
                self.resetTopIcePos()
                self.scoopStack.append(IceCreamStackItem(iceIndex=i.kind))

    # スプーンを追加
    def addSpoon(self):
        if self.spoonButton.isClicked():
            self.resetTopIcePos()
            self.scoopStack.append(IceCreamStackItem(tag="spoon"))

    # アイスのボタンを生成
    def makeIceButtons(self) -> list[IceButton]:
        iceButtons_list = []
        for i in range(7):
            iceButtons_list.append(IceButton(
                x=31+(i//4*16)+(i%4)*16, y=156+i//4*16, kind=i))
        return iceButtons_list

    # カウントアップをスタート
    def startCount(self):
        self.startTime = pyxel.frame_count

    # 制限時間が訪れたか
    def isTimeLimit(self) -> bool:
        return self.LIMIT_TIME - (pyxel.frame_count - self.startTime) < 0

    # 条件に沿ったら、ゲームを終了させる
    def finishGame(self):
        if self.isTimeLimit():
            self.gameState = GameState.TRANS_TO_SCORE

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
            posX = x
            posY = y-i*10
            # てっぺんだけ落とすアニメーションをつける
            if i == len(self.scoopStack)-1:
                posY = self.topIcePos[1]
                if posY < y-i*10:
                    self.vy += self.G
                    posY += self.vy
                    self.topIcePos[1] = posY
                else:
                    posY = y-i*10
            if crtItem.tag == "ice":
                # アイスをちょっとずらす
                if i != 1:
                    posX += 1 if i%2 else -1
                Ice(posX, posY, crtItem.iceIndex).draw()
            elif crtItem.tag == "spoon":
                SpoonButton(posX, posY).draw()
            else:
                if i == 0:
                    if crtItem.tag == "cup": Cup(y=102).draw()
                    elif crtItem.tag == "cone": Cone(y=102).draw()

    # てっぺんのアイスの落下アニメーション用の座標をリセット
    def resetTopIcePos(self):
        self.topIcePos: list[float] = [47, 0]
        self.vy: float = 0

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

    # 売り上げを加算
    def increaseCapital(self):
        point = 10 + len(self.scoopStack)
        self.capitalSnack = CapitalSnack(point=point, corrected=True, exist=True)
        self.capital += point
        self.makeOrder()

    # 売り上げを減算
    def decreaseCapital(self):
        point = (10 + len(self.scoopStack)) // 2
        self.capitalSnack = CapitalSnack(point=point, corrected=False, exist=True)
        self.capital -= point

    # アイスクリームを給仕
    def serveProduct(self):
        if self.serve.isClicked():
            if self.checkProduct():
                self.increaseCapital()
            else:
                self.decreaseCapital()
            self.scoopStack = []

    # 現在資金を表示
    def drawCapital(self):
        pyxel.text(88, 4, f'${self.capital}', 7)

    # 残り時間を描画
    def drawRestTime(self):
        restCol: int = 7
        REST_TIME_RATIO: float = 1 - (pyxel.frame_count - self.startTime) / self.LIMIT_TIME
        # 割合に応じて、ゲージの色を変える
        if REST_TIME_RATIO < 0.3:
            restCol = 8
        elif REST_TIME_RATIO < 0.5:
            restCol = 10
        pyxel.rect(5, 4, 30 * REST_TIME_RATIO, 8, restCol)

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

    # 「タップでスタート」
    def tapToStart(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.startCount()
            self.gameState = GameState.GAME

    def tapToEnd(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.gameState = GameState.FINISHED

    # 「タップでスタート」を描画
    def drawTapToStart(self):
        if pyxel.frame_count % 60 < 50:
            pyxel.text(30, 140, "Tap To Start", 7)

    # 終了を描画
    def drawFinished(self):
        pyxel.blt(16, 38, 2, 0, 8, 87, 63, colkey=0)
        if pyxel.frame_count % 60 < 50:
            pyxel.text(35, 140, "Tap To End", 7)

    def update(self) -> bool:
        if self.gameState == GameState.GAME:
            self.scoopIce()
            self.serve.update()
            self.serveProduct()
            self.pushCupOrCone()
            self.addSpoon()
            self.capitalSnack.update()
            self.finishGame()
            return False
        elif self.gameState == GameState.TAP_TO_START:
            self.tapToStart()
            return True
        elif self.gameState == GameState.TRANS_TO_SCORE:
            return False
        elif self.gameState == GameState.FINISHED:
            self.finished = True
            return True

    def draw(self):
        pyxel.cls(1)
        if self.gameState == GameState.GAME:
            self.drawControllPanel()
            self.serve.draw()
            self.order.draw()
            self.drawScoopedIce()
            self.capitalSnack.draw()
            self.drawCapital()
            self.drawRestTime()
        elif self.gameState == GameState.TAP_TO_START:
            self.order.draw()
            self.drawControllPanel()
            self.drawTapToStart()
        elif self.gameState == GameState.TRANS_TO_SCORE:
            self.order.draw()
            self.drawControllPanel()
            self.drawFinished()
            self.tapToEnd()

