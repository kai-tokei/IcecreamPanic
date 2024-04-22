import pyxel

class App:
    def __init__(self):
        pyxel.init(108, 192, fps=60)
        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
