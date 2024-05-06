# modules
import pyxel

# object
from objects.game import Game

class App:
    def __init__(self):
        self.Game = Game()
        pyxel.init(108, 192, fps=60)
        pyxel.load("assets/icecream.pyxres")
        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.Game.update()

    def draw(self):
        self.Game.draw()
