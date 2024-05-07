class RectField:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height

    def getSize(self):
        return tuple(self.width, self.height)

    def getType(self):
        return "rect"

    def isInside(self, x: int, y: int):
        xInside = self.x <= x <= self.x
        yInside = self.y <= y <= self.y
        return xInside and yInside
