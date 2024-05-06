# modules
import pyxel

# object
from objects.manager import Manger

class App:
    def __init__(self):
        self.manager = Manger()
        pyxel.init(108, 192, fps=60)
        pyxel.load("assets/icecream.pyxres")
        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.manager.update()

    def draw(self):
        self.manager.draw()
