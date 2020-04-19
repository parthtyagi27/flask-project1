from card import Card

class Game:
    playerList = None
    cards = None

    def __init__(self):
        self.playerList = []
        self.cards = []
        colors = ['red', 'blue', 'green', 'yellow']
        action_cards = ['skip', '+2', 'reverse']
        wild_cards = ['color', '+4']
        for color in colors:
            zero_card = Card("0", color)
            self.cards.append(zero_card)
            for i in range(9):
                new_Card_1 = Card(i + 1, color)
                new_Card_2 = Card(i + 1, color)
                self.cards.append(new_Card_1)
                self.cards.append(new_Card_2)
            for action in action_cards:
                new_Card_1 = Card(action, color)
                new_Card_2 = Card(action, color)
                self.cards.append(new_Card_1)
                self.cards.append(new_Card_2)
        for wild in wild_cards:
            for i in range(4):
                new_Card = Card(wild, "wild")
                self.cards.append(new_Card)

        print("Listing Cards:")
        for i in range(len(self.cards)):
            print(str(self.cards[i]))
        


    def addPlayer(self, playerObj):
        self.playerList.append(playerObj)

    def addPlayers(self, playerObjList):
        self.playerList.extend(playerObjList)

    def inGame(self, playerObj):
        for i in range(len(self.playerList)):
            if (self.playerList[i].getIP() == playerObj.getIP()):
                return True
        return False
    
    def getPlayers(self, ip):
        if (self.inGame(ip) == False):
            return None
        else:
            players = list(list())
            for i in range(len(self.playerList)):
                players[i]['name'] = self.playerList[i][0]
                players[i]['ip'] = self.playerList[i][1]

            return players

    def startGame(self):
        return None