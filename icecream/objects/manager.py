import json
import pyxel
from consts.scene import Scene

from scenes.game import Game
from scenes.title import Title
from scenes.score import Score

class Manager:
    def __init__(self) -> None:
        self.scene = Scene.TITLE
        self.sounds: dict = {}

        # Sceneの読み込み
        self.game: Game = Game()
        self.title: Title = Title()
        self.score: Score = Score()

        # bgmの読み込み
        self.addSound("title", "title")
        self.addSound("game", "game")
        self.isSetSound: bool = False

        self.capital: int = 0

    def setScene(self, scene: Scene):
        self.scene = scene

    def addSound(self, name: str, path: str):
        with open(f"./assets/sounds/{path}.json", "rt") as fin:
        #with open(f"icecream/assets/sounds/{path}.json", "rt") as fin:
            self.sounds[name] = json.loads(fin.read())

    def stopSound(self):
        self.isSetSound = False
        pyxel.stop()

    def playSound(self, name: str, loop=False):
        if not self.isSetSound:
            if pyxel.play_pos(0) is None:
                for ch, sound in enumerate(self.sounds[name]):
                    pyxel.sound(ch).set(*sound)
                    pyxel.play(ch, ch, loop=loop)
                self.isSetSound = True
            else:
                self.stopSound()

    def update(self):
        if self.scene == Scene.GAME:
            if self.game.update():
                self.stopSound()
                # self.capital = self.game.capital
                # self.scene = Scene.SCORE
            else:
                self.playSound("game", True)
        elif self.scene == Scene.TITLE:
            if self.title.update():
                self.scene = Scene.GAME
                self.stopSound()
            else:
                self.playSound("title", True)
            self.playSound("title", True)
        elif self.scene == Scene.SCORE:
            self.playSound("title", True)

    def draw(self):
        if self.scene == Scene.GAME:
            self.game.draw()
        elif self.scene == Scene.TITLE:
            self.title.draw()
        elif self.scene == Scene.SCORE:
            self.score.draw()
