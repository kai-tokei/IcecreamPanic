import pyxel

class Button:
    def __init__(self, x: int, y: int, width: int=10, height: int=10) -> None:
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height

    def isInside(self, x: int, y: int):
        xInside: bool = (self.x <= x) and (x <= self.x + self.width)
        yInside: bool = (self.y <= y) and (y <= self.y + self.height)
        return xInside and yInside

    def isClicked(self):
        return pyxel.btnp(
            pyxel.MOUSE_BUTTON_LEFT) and self.isInside(pyxel.mouse_x, pyxel.mouse_y)
