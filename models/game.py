from ..data_loader import (load_pieces, load_spaces, load_CommunityChest, load_Chance, load_properties)

class Game(object):
    def __init__(self, x):
        self.pieces = load_pieces()
        self.spaces = load_spaces()
        self.cards = {}
        self.cards['CommunityChest'] = load_CommunityChest()
        self.cards['Chance'] = load_Chance()
        self.properties = load_properties()
