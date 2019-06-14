from ..data_loader import (load_pieces, load_spaces, load_deck, load_properties)


class Game(object):
    def __init__(self, x):
        self.pieces = load_pieces()
        self.spaces = load_spaces()
        self.cards = {'CommunityChest': load_deck('community_chest'), 'Chance': load_deck('chance')}
        self.properties = load_properties()
