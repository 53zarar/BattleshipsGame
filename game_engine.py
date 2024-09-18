from components import create_battleships, initialise_board, place_battleships
from typing import List, Dict, Any, Union, Tuple

def attack(coordinates: Tuple[int, int], board: List[List[Union[None, str]]], battleships: Dict[str, int])\
    -> Tuple[bool, bool]:
    '''Attacks specific coordinates and if the there is a ship at coordinates, it is replaced with value None. 
    Also checks if the ship has sunk.'''
    x, y = coordinates
    # iterates through battleships to check if there in a ship and the coordinates
    if board[x][y] in battleships:
        ship = board[x][y]
        # assigns None to place where ship was hit
        board[x][y] = None
        # ship is sunk when the battleship's length is 0
        is_sunk = battleships[ship] == 0
        return True, is_sunk
    else:
        # if coordinates don't have a ship
        return False, False

def cli_coordinates_input() -> Tuple[int, int]:
    '''Allows the user to enter coordinates for the custom attack and checks if they are within the size of the 
    board'''
    while True:
        try:
            # asks the user to enter coordinates
            x = int(input("Enter X coordinate: "))
            y = int(input("Enter Y coordinate: "))
            # checks if coordinates are within the board's size, 0 and 9
            if 0 <= x < 10 and 0 <= y < 10:
                return x, y
            # returns message if coordinates aren't in the range
            else:
                print("Invalid coordinates. Please enter values within the valid range.")
        # if integers aren't entered
        except ValueError:
            print("Invalid input. Please enter numerical values for coordinates.")

def simple_game_loop() -> None:
    '''Prints a message to welcome the user to the game. Creates the board and battleships. Places the ships on the boards, 
    and allows user to enter coordinates, and shoot at those coordinates. Displays whether or not they hit a ship, and if 
    they sunk a ship. Prints game over when all ships are sunk. '''
    print('Welcome to Battleships!')
    
    #creates ships and board
    board = initialise_board()
    ships = create_battleships()

    #converts ship sizes to integers
    ships = {ship: int(size) for ship, size in ships.items()}

    #places battleships on board
    place_battleships(board, ships)

    #continues the games till all ships are sunk
    while any(ships.values()):
        print("Current board:")
        for row in board:
            print(row)

        #prompts the user to enter coordinates and carrier out attack
        x, y = cli_coordinates_input()
        hit, sunk = attack((x, y), board, ships)
        if hit:
            print('Hit!')
            if sunk: 
                print('You sunk a battleship!')
        else: 
            print('Miss!')
    
    print('Game Over!')

if __name__ == "__main__":
    simple_game_loop()