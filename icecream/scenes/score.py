import pyxel
import random
from components.ice import Ice

class Score:
    def __init__(self) -> None:
        self.capital: int = 0
        self.ices: list[Ice] = []

    def spawnIce(self):
        ice = Ice(x=random.randint(16, 92), y = -30, kind = random.randint(0, 8))
        self.ices.append(ice)

    def update(self, capital: int):
        self.capital = capital
        self.cleanIce()
        if not pyxel.frame_count % 30:
            self.spawnIce()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return False
        return True

    def cleanIce(self):
        for ice in self.ices:
            if (ice.y > 192):
                self.ices.remove(ice)

    def drawIce(self):
        for i in range(len(self.ices)):
            self.ices[i].y += abs(self.ices[i].y / 30) + 1
            self.ices[i].draw()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(30, 80, "Your score is", 7)
        pyxel.text(48, 100, f"${self.capital}", 7)
        self.drawIce()
        if pyxel.frame_count % 60 < 50:
            pyxel.text(27, 160, "Tap to restart", 7)
