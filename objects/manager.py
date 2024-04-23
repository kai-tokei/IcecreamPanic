import pyxel

# Components
from components.button.cone_button import ConeButton
from components.button.cup_button import CupButton
from components.button.ice_button import IceButton
from components.cone import Cone
from components.cup import Cup
from components.speech_bubble import SpeechBubble
from components.serve import Serve

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
        self.cupButton = CupButton(8, 146)
        self.coneButton = ConeButton(8, 167)

        self.speech = SpeechBubble()
        self.serve = Serve()

        self.capital: int = 100  # 資金($)
        self.scoopStack: list[any] = []  # 今作っているアイスクリームのスタック
        self.orderStack: list[any] = []  # 注文されたアイスクリームのスタック

    def update(self):
        [i.update() for i in self.iceButtons_list]

    def draw(self):
        pyxel.cls(0)
        self.cupButton.draw()
        self.coneButton.draw()
        [i.draw() for i in self.iceButtons_list]
        self.speech.draw()
        self.serve.draw()
