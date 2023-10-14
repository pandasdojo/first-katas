import unittest

from bowling_kata.game import Game


class TestBowlingGame(unittest.TestCase):
    def setUp(self) -> None:
        self._g = Game()

    # Metodo utilitario de teste
    def roll_many(self, n, pins):
        i = 0
        # reforar usando listcomp
        while i < n:
            self._g.roll(pins)
            i += 1

    # gutter: canaleta; gutter game: jogo onde a bola vai pra canaleta (nao derruba pino)
    def test_gutter_game(self):
        self.roll_many(n=20, pins=0)
        self.assertEqual(0, self._g.score())

    def test_all_ones(self):
        self.roll_many(n=20, pins=1)
        self.assertEqual(20, self._g.score())


"""
Game: feito de 10 Frames (Rodadas)
Frame: feito de 2 tentativas de lançamento de bola (Roll)
Pinos: cada Frame tem 10 pinos
Caso de Strike: se derrubar 10 pinos na primeira Roll
    Score: 10 + score das duas proximas jogadas (rolls)
Caso de Spare: se só conseguir derrubar 10 pinos na segunda tentativa (roll)
    Score: 10 + score da proxima jogada (roll)
Caso Especial do 10o Frame:
    Se fizer Strike: dá direito a 2 jogadas extras (bola extra / extra roll)
    Se fizer Spare: dá direito a 1 jogada extra
    
    
Caso do 'Johnny'

Frame #1
  roll #1: 1
  roll #2: 4
  score: 1 + 4 = 5
  
Frame #2
  roll #3: 4
  roll #4: 5
  score do frame: 4 + 5
  score: 5 + (4 + 5) = 14

Frame #3 [SPARE]
  roll #5: 6
  roll #6: 4
  score do frame: 6 + 4 = 10
  score: 14 + 1R = 14 + 10 + 5 = 29

Frame #4 [SPARE]
  roll #7: 5
  roll #8: 5
  score: 29 + 1R + 10 = 39 + 10 = 49

Frame #5 [STRIKE]
  roll #9: 10
  score: 49 + 10 + 2R = 59 + 1 = 60

Frame #6
  roll #10: 0
  roll #11: 1
  score: 60 + 1 = 61

Frame #7 [SPARE]
  roll #12: 7
  roll #13: 3
  score: 61 + 10 + 1R = 71 + 6 = 77

Frame #8 [SPARE]
  roll #14: 6
  roll #15: 4
  score: 77 + 10 + 1R = 87 + 10 = 97

Frame #9 [STRIKE]
  roll #16: 10
  score: 97 + 10 + 2R = 107 + 10 = 117

Frame #10 [SPARE]
  roll #17: 2
  roll #18: 8
  roll #19: 6
  score: 117 + 10 + 6 = 133
  
Caso em que Johnny virou um exímio jogador. Ele vai fazer um Perfect Game.

Frame #1 [STRIKE]
  roll #1: 10
  score: 10 + 2R = 10 + 10 + 10 = 30

Frame #2 [STRIKE]
  roll #2: 10
  score: 30 + 10 + 2R = 40 + 2R = 40 + 20 = 60
  
Frame #3 [STRIKE]
  roll #3: 10
  score: 60 + 10 + 2R = 70 + 2R = 70 + 20 = 90
  
Frame #4 [STRIKE]
  roll #4: 10
  score: 90 + 10 + 2R = 100 + 2R = 100 + 20 = 120
  
Frame #5 [STRIKE]
  roll #5: 10
  score: 120 + 10 + 2R = 130 + 2R = 130 + 20 = 150

Frame #6 [STRIKE]
  roll #6: 10
  score: 150 + 10 + 2R = 160 + 2R = 160 + 20 = 180
 
Frame #7 [STRIKE]
  roll #7: 10
  score: 180 + 10 + 2R = 190 + 2R = 190 + 20 = 210
  
Frame #8 [STRIKE]
  roll #8: 10
  score: 210 + 10 + 2R = 220 + 2R = 220 + 20 = 240

Frame #9 [STRIKE]
  roll #9: 10
  score: 240 + 10 + 2R = 250 + 2R = 250 + 20 = 270

Frame #10 [STRIKE]
  roll #10: 10
  roll #11: 10 (extra)
  roll #12: 10 (extra)
  score: 270 + 30 = 300
"""