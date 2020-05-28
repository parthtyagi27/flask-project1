from card import Card
import random

class Game:

    def __init__(self):
        self.playerList = []
        self.cards = list()
        self.disposedCards = list()
        self.currentCard = None
        self.reverse_factor = 1
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
                card = self.cards.pop(card_index)
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
        
        self.cards.pop(starting_card_index)
        self.disposedCards.append(starting_card)
        self.currentCard = starting_card

    def gameStarted(self):
        if self.turn == None:
            return False
        return True

    def getTurn(self):
        return self.turn

    def nextPlayer(self):
        self.turn = self.turn + (1 * self.reverse_factor)
        if (self.turn == len(self.playerList)):
            self.turn = 0
        elif self.turn == -1:
            self.turn = len(self.playerList) - 1
        return self.turn

    def getPlayer(self, index):
        return self.playerList[index]

    def getNextPlayer(self):
        if (self.turn + 1 == len(self.playerList)):
            return self.playerList[0]
        else:
            return self.playerList[self.turn + 1]

    def getCurrentCard(self):
        return self.currentCard

    def setCurrentCard(self, id, player, color = "keep"):
        # self.currentCard = self.cards[id]
        playerCards = self.getPlayerCards(player)
        print("Player cards = " + str(playerCards))
        for i in range(len(playerCards)):
            print(playerCards[i])
            if playerCards[i].getCardID() == id:
                print("Removing " + str(playerCards[i]))
                self.currentCard = playerCards.pop(i)
                break
        if self.currentCard.isActionCard() == True:
            if self.currentCard.getValue() == "+2" or self.currentCard.getValue() == "+4":
                nextPlayer = self.getNextPlayer()
                if self.currentCard.getValue() == "+2":
                    self.pickUpCard(nextPlayer)
                    self.pickUpCard(nextPlayer)
                elif self.currentCard.getValue() == "+4":
                    self.pickUpCard(nextPlayer)
                    self.pickUpCard(nextPlayer)
                    self.pickUpCard(nextPlayer)
                    self.pickUpCard(nextPlayer)
            elif self.currentCard.getValue() == "skip":
                self.nextPlayer()
            elif self.currentCard.getValue() == "reverse":
                self.reverse_factor = self.reverse_factor * -1

            if color != "keep":
                self.currentCard.setColor(color)
                print("Set current card color to " + self.currentCard.getColor())


    def pickUpCard(self, user):
        card_index = random.randint(0, len(self.cards) - 1)
        self.getPlayerCards(user).append(self.cards.pop(card_index))
