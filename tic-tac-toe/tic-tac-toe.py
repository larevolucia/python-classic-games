#!/usr/bin/env python3

from pprint import pprint
import random

def print_board(board):
    print(f'{board["top-l"]} | {board["top-m"]} | {board["top-r"]}')
    print('--------- ')
    print(f'{board["mid-l"]} | {board["mid-m"]} | {board["mid-r"]}')
    print('---------')
    print(f'{board["low-l"]} | {board["low-m"]} | {board["low-r"]}')

def greet_user():
    print("Hello there! What's your name?")
    name = input()
    invite_for_game(name)

def goodbye():
    print('See you later!')

def find_best_move(board):
    # Win: If there's a move that wins the game, take it.
    for move in board.keys():
        if board[move] == " ":
            board[move] = "O"
            if check_winner(board) == "O":
                return move
            board[move] = " "
    # Block: If the opponent has a move that can win the game, block it.
    for move in board.keys():
        if board[move] == " ":
            board[move] = "X"
            if check_winner(board) == "X":
                board[move] = " "
                return move
            board[move] = " "

    # Center: Play the center if it's available.
    if board["mid-m"] == " ":
        return "mid-m"
    
    # Opposite Corner: If the opponent is in a corner, play the opposite corner.
    corners = [("top-l", "low-r"), ("top-r", "low-l"), ("low-l", "top-r"), ("low-r", "top-l")]
    for corner, opposite in corners:
        if board[corner] == "X" and board[opposite] == " ":
            return opposite
        
    # Empty Corner: Play an empty corner
    corner_positions = ["top-l", "top-r", "low-l", "low-r"]
    empty_corners = [position for position in corner_positions if board[position] == " "]
    if empty_corners:
        return random.choice(empty_corners)
    
    # Empty Side: Play an empty side.
    sides_positions = ["top-m", "mid-l", "mid-r", "low-m"]
    empty_sides = [position for position in sides_positions if board[position] == " "]
    if empty_sides:
        return random.choice(empty_sides)    
    
    # If no other move is possible (should not reach here in a typical game)
    return random.choice([key for key, value in board.items() if value == " "])

def make_move(board_game, player):
    if player == "X":
        print("Where would you like to set your X?")
        print("Choose between: top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R")
        move = input().strip().lower()
        while move not in board_game or board_game[move] != " ":
            print("Invalid move. Try again.")
            move = input().strip().lower()
    else:
        is_strategic = random.choice([True, False])
        print(is_strategic)
        if is_strategic:
            move = find_best_move(board_game)
            print(f"Computer chose {move}")
        else:
            move = random.choice([key for key, value in board_game.items() if value == " "])
            print(f"Computer chose {move}")

    board_game[move] = player
    print_board(board_game)

def check_winner(board):
    winning_combinations = [
        ["top-l", "top-m", "top-r"],
        ["mid-l", "mid-m", "mid-r"],
        ["low-l", "low-m", "low-r"],
        ["top-l", "mid-l", "low-l"],
        ["top-m", "mid-m", "low-m"],
        ["top-r", "mid-r", "low-r"],
        ["top-l", "mid-m", "low-r"],
        ["top-r", "mid-m", "low-l"]
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    
    if " " not in board.values():
        return "Tie"
    
    return None

def launch_game(name):
    board_game = {
        "top-l": " ",
        "top-m": " ",
        "top-r": " ",
        "mid-l": " ",
        "mid-m": " ",
        "mid-r": " ",
        "low-l": " ",
        "low-m": " ",
        "low-r": " "
    }
    print("Let's start!")
    print_board(board_game)

    current_player = "X"
    for i in range(9):
        make_move(board_game, current_player)
        winner = check_winner(board_game)
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            elif winner == "X":
                print(f"{name} wins!")
            else:
                print("Computer wins!")
            return
        current_player = "O" if current_player == "X" else "X"
    
    print("Game over!")

def invite_for_game(name):

   while True:
        print(f'Would you like to play a tic-tac-toe game, {name}? (yes/no)')
        answer = input().lower()
        if answer == "yes":
            print("I'll be O and you'll be X.")
            launch_game(name)
        elif answer == "no":
            goodbye()
        else:
            print("Sorry, I didn't understand.")

if __name__ == "__main__":
    greet_user()
    input("Press Enter to exit...")
