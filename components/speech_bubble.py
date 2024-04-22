import pyxel
from objects.gameobject import GameObject

class SpeechBubble(GameObject):
    def __init__(self, x: float=15, y: float=15):
        super().__init__(x, y)
        self.radius = 22

    def udpate(self):
        pass

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, col=7)

