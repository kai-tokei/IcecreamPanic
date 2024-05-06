from consts.scene import Scene
from scenes.game import Game

class Manger:
    def __init__(self) -> None:
        self.scene = Scene.TITLE
        #self.scene = Scene.GAME
        self.game = Game()

    def update(self):
        if self.scene == Scene.GAME:
            self.game.update()

    def draw(self):
        if self.scene == Scene.GAME:
            self.game.draw()

