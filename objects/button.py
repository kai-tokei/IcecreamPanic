import pyxel

class Button:
    def __init__(self, x: int, y: int, width: int=0, height: int=0) -> None:
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height

    def isInside(self, x: int, y: int):
        xInside = self.x <= x <= self.x + self.width
        yInside = self.y <= y <= self.y + self.height
        return xInside and yInside

    def isClicked(self, x: int, y: int):
        return pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.isInside(x, y)
