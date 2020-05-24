from card import Card
import random

class Game:

    def __init__(self):
        self.playerList = []
        self.cards = list()
        self.disposedCards = list()
        self.currentCard = None
        colors = ['red', 'blue', 'green', 'yellow']
        action_cards = ['skip', '+2', 'reverse']
        wild_cards = ['color', '+4']
        for color in colors:
            zero_card = Card("0", color, False)
            self.cards.append(zero_card)
            for i in range(9):
                new_Card_1 = Card(i + 1, color, False)
                new_Card_2 = Card(i + 1, color, False)
                self.cards.append(new_Card_1)
                self.cards.append(new_Card_2)
            for action in action_cards:
                new_Card_1 = Card(action, color, True)
                new_Card_2 = Card(action, color, True)
                self.cards.append(new_Card_1)
                self.cards.append(new_Card_2)
        for wild in wild_cards:
            for i in range(4):
                new_Card = Card(wild, "wild", True)
                self.cards.append(new_Card)

        # print("Listing Cards:")
        # for i in range(len(self.cards)):
        #     print(str(self.cards[i]))

        self.turn = None
        

    def addPlayer(self, playerObj):
        self.playerList.append(playerObj)

    def addPlayers(self, playerObjList):
        self.playerList.extend(playerObjList)

    def inGame(self, playerObj):
        for i in range(len(self.playerList)):
            if (self.playerList[i].getIP() == playerObj.getIP()):
                return True
        return False
    
    def getPlayers(self):
        # if (self.inGame(ip) == False):
        #     return None
        # else:
        #     players = list(list())
        #     for i in range(len(self.playerList)):
        #         players[i]['name'] = self.playerList[i][0]
        #         players[i]['ip'] = self.playerList[i][1]

        #     return players
        return self.playerList

    def getPlayerCards(self, player):
        if len(player.getCards()) == 0:
            # generate cards for the player
            cards = list()
            for i in range(7):
                card_index = random.randint(0, len(self.cards) - 1)
                card = self.cards[card_index]
                cards.append(card)
            player.setCards(cards)

        return player.getCards()

    def startGame(self):
        turn_index = random.randint(0, len(self.playerList) - 1)
        self.turn = turn_index

        starting_card_index = random.randint(0, len(self.cards) - 1)
        starting_card = self.cards[starting_card_index]

        while starting_card.isActionCard() == True:
            starting_card_index = random.randint(0, len(self.cards) - 1)
            starting_card = self.cards[starting_card_index]
        
        self.disposedCards.append(starting_card)
        self.currentCard = starting_card

    def gameStarted(self):
        if self.turn == None:
            return False
        return True

    def getTurn(self):
        return self.turn

    def nextPlayer(self):
        self.turn = self.turn + 1
        if (self.turn == len(self.playerList)):
            self.turn = 0
        return self.turn

    def getPlayer(self, index):
        return self.playerList[index]

    def getCurrentCard(self):
        return self.currentCard

    def setCurrentCard(self, id, player):
        self.currentCard = self.cards[id]
        playerCards = self.getPlayerCards(player)
        print("Player cards = " + str(playerCards))
        for i in range(len(playerCards)):
            print(playerCards[i])
            if playerCards[i].getCardID() == id:
                print("Removing " + str(playerCards[i]))
                playerCards.pop(i)
                return