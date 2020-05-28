class Card(object):
    
    card_id = 0

    def __init__(self, value, color, isActionCard):
        super()
        self.value = value
        self.color = color
        self.card_id = Card.card_id
        self.action_card = isActionCard
        self.json = {"id" : self.card_id, "color" : self.color, "value": self.value, "action": self.action_card}
        Card.card_id = Card.card_id + 1

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def getAsDict(self):
        return self.json

    def isActionCard(self):
        return self.action_card

    def getCardID(self):
        return self.card_id

    def setColor(self, color):
        self.color = color
        self.json = {"id" : self.card_id, "color" : self.color, "value": self.value, "action": self.action_card}


    def __str__(self):
        return str(self.card_id) + " " + str(self.value) + " " + str(self.color)

    def __repr__(self):
        return str(self.card_id) + " " + str(self.value) + " " + str(self.color)