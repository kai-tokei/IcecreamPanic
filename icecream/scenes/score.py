import pyxel

class Score:
    def __init__(self) -> None:
        self.capital: int = 0

    def update(self, capital: int):
        self.capital = capital
        return False

    def draw(self):
        pyxel.cls(1)
        pyxel.text(30, 80, "Your score is", 7)
        pyxel.text(48, 100, f"${self.capital}", 7)
