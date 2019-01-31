import json
from random import shuffle

def load_pieces():
    pcsFile = 'data/pieces.json'
    with open(pcsFile) as f:
        data = json.load(f)
    pieces = data['pieces']
    shuffle(pieces)
    return pieces

def load_spaces():
    spcFile = 'data/spaces.json'
    with open(spcFile) as f:
        data = json.load(f)
    return data['spaces']

def load_CommunityChest():
    CCfile = "data/community_chest.json"
    with open(CCfile) as f:
        data = json.load(f)
    CC = data['cards']
    shuffle(CC)
    return CC

def load_Chance():
  chanceFile = "data/chance.json"
  with open(chanceFile) as f:
      data = json.load(f)
  C = data['cards']
  shuffle(C)
  return C

def load_properties():
    propFile = "data/properties.json"
    with open(propFile) as f:
        data = json.load(f)
    return data['properties']

def load_data():
    pieces = load_pieces()
    spaces = load_spaces()
    CommunityChest = load_CommunityChest()
    Chance = load_Chance()
    properties = load_properties()
