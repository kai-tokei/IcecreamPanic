from consts.scene import Scene

from scenes.game import Game
from scenes.title import Title

class Manger:
    def __init__(self) -> None:
        self.scene = Scene.TITLE
        #self.scene = Scene.GAME
        self.game = Game()
        self.title = Title()

    def update(self):
        if self.scene == Scene.GAME:
            self.game.update()
        elif self.scene == Scene.TITLE:
            self.title.update()

    def draw(self):
        if self.scene == Scene.GAME:
            self.game.draw()
        elif self.scene == Scene.TITLE:
            self.title.draw()

