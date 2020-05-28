import sys
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
                    if len(game.getPlayers()) == len(users):
                        if game.gameStarted() == False:
                            game.startGame()
                    return render_template('game.html')
                else:
                    return render_template('game.html')

@app.route('/updateGame', methods=['GET', 'POST'])
def updateGame():
    print("\n")
    print("RECIEVED UPDATE GAME REQUEST FROM " + str(request.remote_addr))
    #check if requester is a user
    user = None
    for i in range(len(users)):
        if (users[i].getIP() == request.remote_addr):
            if (game.inGame(users[i]) == True):
                user = users[i]
    if user == None:
        return 'Error', 500
    if (request.method == 'GET'):
        # print("RECIEVED UPDATE GAME REQUEST FROM " + str(request.remote_addr))
        # #check if requester is a user
        # user = None
        # for i in range(len(users)):
        #     if (users[i].getIP() == request.remote_addr):
        #         if (game.inGame(users[i]) == True):
        #             user = users[i]
        # if user == None:
        #     return 'Error', 500

        #check if query contains get cards line
        print("GET REQUEST!")
        query_string = request.query_string
        response = list()
        info_query_string = request.args.get("info")
        # info_queries = []
        # # test how the query looks like with csv formatting
        # print(query)
        # if query == "cards":
        #     player_cards = game.getPlayerCards(user)
        #     for card in player_cards:
        #         response.append(card.getAsDict())
        #     json = jsonify({'cards' : response}) 
        #     print(json.get_json())
        #     return json
        # if query == "turn":
        #     # add get turn code
        #     return
        info_queries = info_query_string.split(",")
        print("Info queries = " + str(info_queries))
        for info_query in info_queries:
            if info_query == "cards":
                cards_list = list()
                player_cards = game.getPlayerCards(user)
                for card in player_cards:
                    cards_list.append(card.getAsDict())
                cards_dict = {'cards' : cards_list} 
                # print(cards_dict)
                # response.append(cards_dict)
                response.append({'cards': cards_list})
            if info_query == "turn":
                if game.gameStarted() == False:
                    game.startGame()
                # turn_response = {"turn": game.getTurn()}
                # response.append(turn_response)
                response.append({'turn': game.getPlayer(game.getTurn()).getName()})
            if info_query == "currentCard":
                response.append({'currentCard': game.getCurrentCard().getAsDict()})
            if info_query == "winner":
                response.append({'winner': game.getWinner()})
        if len(response) == 0:
            return 'No update generated', 200
        else:
            # print(jsonify({response}).get_json())
            return jsonify(response)
        # return 'OK', 200
    elif request.method == 'POST':
        print("POST REQUEST!")
        update_json = request.get_json()
        if update_json['action'] == "playCard":
            card_json = update_json['card']
            print("Playing card = " + str(card_json))
            if len(update_json) == 2:
                print("Playing normal card")
                game.setCurrentCard(card_json['id'], user)
            elif len(update_json) == 3:
                print("Playing wild card")
                game.setCurrentCard(card_json['id'], user, update_json['color'])
            game.nextPlayer()
            return 'OK', 200
        elif update_json['action'] == "pickCard":
            print("Pick up Card request!")
            game.pickUpCard(user)
            game.nextPlayer()
            return 'OK', 200



if (__name__ == '__main__'):
    # sys.stdout = sys.stderr = open('server-log.txt', 'wt')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    game = Game.Game()
    app.run(host='0.0.0.0', port=80)