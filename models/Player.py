from models.property import Property

class Player(object):
    def __init__(self):
        self.props = {}
        self.money = 1500

    def addProperty(self, property):
        if type(property) is not Property:
            raise ValueError('Not a valid property!')