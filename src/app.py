# modules
import pyxel

# object
from objects.manager import Manager

class App:
    def __init__(self):
        self.manager = Manager()
        pyxel.init(108, 192, fps=60, title="Icecream Panic")
        pyxel.load("assets/icecream.pyxres")
        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.manager.update()

    def draw(self):
        self.manager.draw()

App()
