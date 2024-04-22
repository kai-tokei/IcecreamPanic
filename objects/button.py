import pyxel

class Button:
    def __init__(self, x: int, y: int, width: int=0, height: int=0) -> None:
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
