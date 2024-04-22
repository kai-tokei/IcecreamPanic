import pyxel

# Components
from components.button.cone_button import ConeButton
from components.button.cup_button import CupButton
from components.button.ice_button import IceButton

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

        self.capital: int = 100  # 資金($)
        self.scoopStack: list[int] = []  # 今作っているアイスクリームのスタック
        self.orderStack: list[int] = []  # 注文されたアイスクリームのスタック

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.cupButton.draw()
        self.coneButton.draw()
        [i.draw() for i in self.iceButtons_list]
