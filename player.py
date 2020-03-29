class Player:
    cards = None
    name = None
    ip = None
    ready = None

    def __init__(self, name, ip):
        self.cards = list()
        self.name = name
        self.ip = ip
        self.ready = False

    def getIP(self):
        return self.ip

    def getName(self):
        return self.name
    
    def isReady(self):
        return self.ready

    def setReady(self):
        self.ready = True