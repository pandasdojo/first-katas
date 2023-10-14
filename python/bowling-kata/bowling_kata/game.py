class Game:
    def __init__(self):
        self._score: int = 0

    def roll(self, pins):
        self._score += pins

    def score(self) -> int:
        return self._score
