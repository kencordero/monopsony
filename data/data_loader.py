import json
from random import shuffle


def load_pieces():
    filename = 'monopsony/data/pieces.json'
    with open(filename) as f:
        data = json.load(f)
    pieces = data['pieces']
    shuffle(pieces)
    return pieces


def load_spaces():
    filename = 'monopsony/data/spaces.json'
    with open(filename) as f:
        data = json.load(f)
    return data['spaces']


def load_deck(deck_type):
    deck_file = 'monopsony/data/{}.json'.format(deck_type)
    with open(deck_file) as f:
        data = json.load(f)
    deck = data['cards']
    shuffle(deck)
    return deck


def load_properties():
    filename = 'monopsony/data/properties.json'
    with open(filename) as f:
        data = json.load(f)
    return data['properties']


def load_data():
    pieces = load_pieces()
    spaces = load_spaces()
    CommunityChest = load_deck('community_chest')
    Chance = load_deck('chance')
    properties = load_properties()
