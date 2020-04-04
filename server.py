from flask import Flask, request, render_template, jsonify, redirect, url_for
import games as Game
import player as Player
import json

app = Flask(__name__)
games = list()
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
        return render_template('game.html')


if (__name__ == '__main__'):
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80)