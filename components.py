import json
import random
from typing import List, Optional, Dict, Any, Union


def initialise_board(size: int = 10) -> List[List[Optional[None]]]:
    '''This function initialises the game board that the AI and Players will use to place 
    their ships and take guesses at'''
     #creates an empty list to contain board
    table = []
    #repeats setting a new row for the value of size amount of times
    for i in range(size): 
        #creates the row for size amount
        row = [None] * size 
        #adds row to board
        table.append(row) 
    return table 


def create_battleships(filename: str = 'battleships.txt') -> Union[Dict[str, Any], None]:
    '''This function creates battleships, which is the name of the ships and thier lengths,
    from reading the battleships.txt file'''
    
    try: 
        #opens and reads the battleship.txt file   
        battleships = eval(open('battleships.txt', 'r').read())
        return battleships
    except FileNotFoundError: 
        #for if file battleship.txt file is not found
        print('File not found:', {filename})#for if file battleship.txt file is not found


def place_battleships(board: List[List[Union[None, str]]], ships: Dict[str, int], algorithm: str = 'random')\
    -> List[List[Union[None, str]]]:
    ''' Places battleships on the boards, for three different placement types, simple, random and custom. 
    For simple if places them on consecutive rows horizontally. For random, it places the ships in random 
    positions and orientations. For custom the player chooses the coordinates and orientations for where to 
    place ships'''
    
    row = 0
    
    if algorithm == 'simple':
    # iterate over each ship in the ships dictionary
        for ship in ships:
            # access the value for the length of the ship, converting it to an integer
            ship_len = int(ships[ship])
            # place the ship on the board by marking its positions in its row
            for column in range(ship_len):
                board[row][column] = ship
            # move to the next row for the next ship placement
            row += 1
    
    elif algorithm == 'random':
        for ship in ships:
            ship_len = int(ships[ship])
            # picks random row from 0 to 9
            rand_row = random.randint(0, 9)
            # picks random column from 0 to 9
            rand_column = random.randint(0, 9)
            # chooses random orientation between horizontal and vertical, or h and v
            ori = random.choice(['h', 'v'])

            #checks if the length of ships is too long to place it
            while (ori == 'h' and rand_column + ship_len > 10) or \
                (ori == 'v' and rand_row + ship_len > 10):
                rand_row = random.randint(0, 9)
                rand_column = random.randint(0, 9)
    
            #iterates for ships lengths
            for i in range(ship_len):
                #adds ship name for the length of ships, either on column or row based on h or v
                if ori == 'h':
                    board[rand_row][rand_column + i] = ship
                elif ori == 'v':
                    board[rand_row + i][rand_column] = ship
   
    elif algorithm == 'custom':
        #opens a json file
        with open('User_Placement.json') as user_placement:
            # loads the file
            custom_dict = json.load(user_placement)
    
            for ship in ships:
                ship_len = int(ships[ship])
            
                # picks the placement coordinates and orientation for the current ship from custom_dict
                firstx = int(custom_dict[ship][0])
                firsty = int(custom_dict[ship][1])
                ori = custom_dict[ship][2]

                for i in range(ship_len):
                    if ori == 'h':
                        board[firsty][firstx + i] = ship
                    elif ori == 'v':
                        board[firsty + i][firstx] = ship

    # returns the modified board after ship placement
    return board
