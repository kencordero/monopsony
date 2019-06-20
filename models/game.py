import sys
from ..data.data_loader import load

MAX_PLAYER_COUNT = 10

class Game(object):
    def __init__(self):
        self.pieces = load('pieces')
        self.spaces = load('spaces')
        self.cards = {'CommunityChest': load('community_chest', 'cards'), 'Chance': load('chance', 'cards')}
        self.properties = load('properties')
        self.config = load('config')
