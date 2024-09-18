# Battleships Game 🚢

This project is a battleships game where you play against an AI. 
There are five battleships of varying lengths.
You win the game by sinking all of the AI's battleships. 
Game is played on a website, and the backend is on Python, while the frontend is on Flask and HTML. 
 
## Installation

This application uses packages that may need to be installed
Python
install Flask
install pytest

Python version used: 3.10.2

## Usage

The four modules in this project are:
1. components.py, functions include initialise_board(), create_battleships() and place_battleships():
    - intialise_board(): Creates a board that is initially empty
    - create_battleships(): Creates a dictionary of battleships, loaded in from the battleships.txt file
    - place_battleships(): Places the battleships onto the board, and can be done with three different elements: simple, random, and custom
 
2. game_engine.py, functions include attack(), cli_coordinates_input() and simple_game_loop():
    - attack(): Processes the attack on a specific coordinate on the board
    - cli_coordinates_input(): Stores the users chosen x and y input for their attack
    - simple_game_loop(): Lets the user play without the AI opponent

3. mp_game_engine.py, functions include generate_attack() and ai_opponent_game_loop():
    - generate_attack(): Generates random coordinates which the AI uses for its attack
    - ai_opponent_game_loop(): Allows the user to play against the AI

4. main.py, functions include root, placement_interface, and process_attack:
    - root: Accessed by "/" is where the main page of the game is set up
    - placement_interface: Accessed by "/placement" is where the user is allowed to place their ships
    - process_attack: Accessed by a GET request to "/attack" where the user's input is handled for the subsequent attack

How to use the application on the web server:
1. Run the main.py file 
2. It will take you to 'http://127.0.0.1:5000', and show the main.html webpage
3. Add '/placement' giving you 'http://127.0.0.1:5000/placement'
4. Place the battleships and press the "Send Board" button
5. Play the game on the main page
6. The game will end if you win or lose

You can also play the game in mp_game_engine.py if you just run that module. 

## License
MIT License

Copyright (c) [2023] [Mohammed Zarrar Shahid]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
