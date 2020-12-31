import pytest
import unittest
import time
import numpy as np
from models.player import *


class TestModels(unittest.TestCase):
    def test_models(self):
        print("start test")
        player1 = Player("Rich", "Harding", "QB", 23, "ATL")
        player2 = Player("Alonzo", "Dunn", "RB", 21, "ATL")

        print(player1)
        print(player2)

    def test_player_comparison(self):
    	print("start test")

if __name__ == '__main__':
    unittest.main()
