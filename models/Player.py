import Property from Property

class Player(object):
    def __init__(self):
        self.props = {}
        self.money = 1500

    def addProperty(self, property):
        if type(property) is a Property:
            raise ValueError('Not a valid property!')