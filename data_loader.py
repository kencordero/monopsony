import json
from random import shuffle

def load_pieces():
    pcsFile = 'pieces.json'
    with open(pcsFile) as f:
        data = json.load(f)
    pieces = data['pieces']
    shuffle(pieces)

def load_spaces():
    spcFile = 'spaces.json'
    with open(spcFile) as f:
        data = json.load(f)
    spaces = data['spaces']

def load_CommunityChest():
    CCfile = "community_chest.json"
    with open(CCfile) as f:
        data = json.load(f)
    CC = data['cards']
    shuffle(CC)

def load_Chance():
  chanceFile = "Chance.txt"
  chanceCards = dict()
  i = 0
  with open(chanceFile) as f:
    for item in f:
      item = item.strip()
      chanceCards[item] = i
      i += 1
  C = chanceCards.keys()
  shuffle(C)

def load_properties():
    propFile = "properties.json"
    i = 0
    with open(propFile) as f:
        data = json.load(f)
    props = data['properties']
