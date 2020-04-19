class Card(object):
    
    card_id = 0

    def __init__(self, value, color):
        super()
        self.value = value
        self.color = color
        self.card_id = Card.card_id
        Card.card_id = Card.card_id + 1

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def __str__(self):
        return str(self.card_id) + " " + str(self.value) + " " + str(self.color)