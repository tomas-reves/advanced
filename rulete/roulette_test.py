import unittest
from roulette_game import RouletteNumberGuessGame, RouletteGameEvenOdd, RouletteGameColumns, RouletteGameDozens, \
    RouletteColorsGame, RouletteGameLowHighNums

class TestCode(unittest.TestCase):
    def test_color_check(self):
        color_ojb = RouletteColorsGame(1)
        self.assertEqual(color_ojb.check_number_color())

