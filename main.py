from flask import Flask, jsonify, render_template, request  
from components import initialise_board, create_battleships, place_battleships
import json
from game_engine import attack
from mp_game_engine import generate_attack 

app = Flask(__name__)

@app.route(rule='/placement', methods =["GET", "POST"])

def placement_interface():
    '''Stores the placement that the user has chosen.
     This is later used in the game logic. '''
    ships = {"Aircraft_Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}

    if request.method == "GET":
        #get request returns placement file
        return render_template("placement.html", ships = ships, board_size= 10)

    if request.method == "POST":
        #storing data passed by post method
        data = request.get_json()

        with open('User_Placement.json', 'w') as placement:
               json.dump(data, placement)

        return jsonify({"message": "hey"}), 200

@app.route(rule="/", methods=["GET"])
def root():
    '''This code is where the main rendering for the main.html page is done'''
    global ships
    #sets boards and ships for both user and AI
    user_board = initialise_board(10)
    ai_board = initialise_board(10)
    ships = create_battleships()
    ships1 = create_battleships()
     
    global players 
    #assigns keys and values to the dictionary players, keys being the players and values being their placement of battleships plus the actual ships
    players = {'user': [place_battleships(user_board, ships, algorithm='custom'), ships], 'AI_opponent': [place_battleships(ai_board, ships, algorithm='random'), ships1]}

    #if method is GET just returns main.html template with the user board
    if request.method == "GET": 
        return render_template('main.html', player_board = players['user'][0])


@app.route(rule = '/attack', methods= ["GET"])
def process_attack(): 
    '''Stores the coordinates inputed by the user and generates the AI's attack. Checks if ships are hit or sunk. 
    Also deals with when all ships are sunk and stops the game when someone wins by sinking all their opponents ships.'''

    #gets the x and y for user's input on the website
    if request.args:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    
    #initiates attack from the users input coordinates
    hit, sunk = attack((x,y), players["AI_opponent"][0], players["AI_opponent"][1])
    
    #generates attack for AI
    AI_coords = generate_attack(10)
    ai_hit, ai_sunk = attack(AI_coords, players["user"][0], players["user"][1])

    #checks if all ships are sunk and then ends the game and declares if the user won or loss, or continues if ships are not sunk
    if all(all(x is None for x in row) for row in players['AI_opponent'][0]):
        return jsonify({"hit": True, "AI_Turn":generate_attack(len(players['user'][0])), 'finished': 'You Won!'})
    if all(all(x is None for x in row) for row in players['user'][0]):
        return jsonify({"hit": True, "AI_Turn":generate_attack(len(players['user'][0])), 'finished': 'You Lost!'})
    else:
        return jsonify({"hit": hit, "AI_Turn": generate_attack(len(players['user'][0]))})
        
if __name__ == '__main__':
    app.template_folder = "template"
    app.run()