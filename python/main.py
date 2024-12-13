"""
Rock Paper Scissors Game In Python
Author: jaypacamarra
Date: Dec 13, 2024
"""

import random

# Constants for the moves
ROCK = 1
PAPER = 2
SCISSORS = 3

# Mapping move numbers to strings
MOVE_TO_STRING = {ROCK: "rock", PAPER: "paper", SCISSORS: "scissors"}

def is_input_valid(user_input):
    """Check if the user input is a valid move (1, 2, or 3)."""
    return user_input in (ROCK, PAPER, SCISSORS)

def get_user_input():
    """Get and validate user input for the game."""
    while True:
        try:
            selected = int(input("Please select [1] rock [2] paper [3] scissors: "))
            if is_input_valid(selected):
                return selected
            else:
                print("Invalid option. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def decide_winner(player_move, computer_move):
    """Determine the winner of the game based on player and computer moves."""
    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == ROCK and computer_move == SCISSORS) or \
         (player_move == PAPER and computer_move == ROCK) or \
         (player_move == SCISSORS and computer_move == PAPER):
        print("Player wins!")
    else:
        print("Computer wins!")

def get_computer_move():
    """Generate a random move for the computer."""
    return random.randint(ROCK, SCISSORS)

def game():
    player_move = get_user_input()
    computer_move = get_computer_move()
    print(f"Player chose {MOVE_TO_STRING[player_move]} ... and the computer chose {MOVE_TO_STRING[computer_move]}")
    decide_winner(player_move, computer_move)

if __name__ == "__main__":
    while True:
        game()

