from flask import Flask, request, render_template, jsonify, redirect, url_for
import games as Game
import player as Player
import json

app = Flask(__name__)
game = Game
users = list()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if (request.method == 'POST'):
        print("Recieved enter post request")
        jsonObj = request.get_json()
        print(jsonObj)
        player = Player.Player(jsonObj['name'], request.remote_addr)
        users.append(player)
        return url_for('lobby')

@app.route('/lobby', methods=['GET'])
def lobby():
    if (len(users) == 0):
        return "You haven't logged in"
    
    ip = request.remote_addr

    for i in range(len(users)):
        if (users[i].getIP() == ip):
            print("Rendering lobby page to user")
            return render_template('lobby.html')

    return "You haven't logged in"

@app.route('/gameInfo', methods=['POST', 'GET'])
def getInfo():
    if (request.method == 'GET'):
        print("\n")
        
        response = list()
        print("RECIEVED INFO REQUEST FROM " + str(request.remote_addr))
        for i in range(len(users)):
            response.append({'name': users[i].getName(), 'ip': users[i].getIP(), 'ready': users[i].isReady()})

        json = jsonify({'players': response})
        print("RESPONSE to " + str(request.remote_addr) + " " + str(json.get_json()))
        return json

@app.route('/ready', methods=['POST', 'GET'])
def ready():
    if (request.method == 'GET'):
        print("\n")
        print("RECIEVED READY REQUEST FROM " + str(request.remote_addr))
        for i in range(len(users)):
            if (users[i].getIP() == request.remote_addr):
                users[i].setReady()
        return 'OK', 200
        
@app.route('/enter', methods=['POST'])
def enterGame():
    if (request.method == 'POST'):
        print("RECIEVED ENTER GAME REQUEST FROM " + str(request.remote_addr))
        if (len(users) == 1):
            return "You need at least 2 people to play!", 500
        for i in range(len(users)):
            if (users[i].isReady == False):
                return "Not everybody is ready yet", 500
        return render_template('game.html')

@app.route('/game', methods=['GET'])
def game():
    if (request.method == 'GET'):
        print("RECIEVED ENTER GAME REQUEST FROM " + str(request.remote_addr))
        for i in range(len(users)):
            if (users[i].getIP() == request.remote_addr):
                if (game.inGame(users[i]) == False):
                    game.addPlayer(users[i])
                    return render_template('game.html')
                else:
                    return "Already in Game", 500

@app.route('/updateGame', methods=['GET'])
def updateGame():
    if (request.method == 'GET'):
        print("RECIEVED Update GAME REQUEST FROM " + str(request.remote_addr))
        #check if query contains get cards line


if (__name__ == '__main__'):
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    game = Game.Game()
    app.run(host='0.0.0.0', port=80)