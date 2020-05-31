import sys
sys.path.insert(0,'..') 

import json
import unittest
from game import Game

class TestDataLoad(unittest.TestCase):    
    @classmethod
    def setUpClass(cls):
        cls._game = Game()

    def test_properties(self):
        self.assertEqual(self._game.properties[14]['name'], 'Kentucky Ave.')

    def test_spaces(self):        
        self.assertEqual(self._game.spaces[9]['name'], 'Connecticut Ave.')

    def test_pieces(self):
        self.assertEqual(len(self._game.pieces), 10)

    def test_cards(self):        
        self.assertEqual(len(self._game.cards['CommunityChest']), 16)    
        self.assertEqual(len(self._game.cards['Chance']), 16)

if __name__ == '__main__':
    unittest.main()