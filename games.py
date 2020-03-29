class Game:
    playerList = None
    cards = None
    def __init__(self):
        self.playerList = list(list())
        self.cards = list(list())

    def addPlayer(self, name, ip):
        playerObj = list()
        playerObj.append(name)
        playerObj.append(ip)
        self.playerList.append(playerObj)

    def inGame(self, ip):
        for i in range(len(self.playerList)):
            if (self.playerList[i][1] == ip):
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