class Card:
    value = None
    color = None
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color