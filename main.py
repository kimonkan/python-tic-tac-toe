############################################ IMPORTING ####################################################

import random

####################################### DEFINING FUNCTIONS ################################################

def game_starting_message():
    start_question = input("Do you want to play?(Y/N)").upper()
    return start_question

def turn_picker():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def marker_assignment():
    player1 = input("Player 1: Do you want to be X or O?").upper()
    while player1 != "X" and player1 != "O":
        player1 = input("Invalid choice. Player 1: Do you want to be X or O? ").upper()
    if player1 == "X":
        player2 = "O"
        print("\nPlayer 2 will be O.")
    else:
        player2 = "X"
        print("\nPlayer 2 will be X.")
    return player1, player2

def marker_placement(board, marker, position):
    board[position] = marker

def win_condition(board, mark, player_turn):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #across the bottom
    (board[4] == mark and board[5] == mark and board[6] == mark) or #across the middle
    (board[7] == mark and board[8] == mark and board[9] == mark) or #across the top
    (board[1] == mark and board[4] == mark and board[7] == mark) or #across the left
    (board[2] == mark and board[5] == mark and board[8] == mark) or #across the middle
    (board[3] == mark and board[6] == mark and board[9] == mark) or #across the right
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal from bottom left to  top right
    (board[3] == mark and board[5] == mark and board[7] == mark)) #diagonal from top left to  bottom right

def display_board(board):
    print("\n" * 100)

    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your next position: (1-9)"))

    return position

def replay():
    return input("Do you want to play again?(Y/N)").upper().startswith("Y")

########################################## GAME STARTING ################################################

print("\nHello there! This is a classic game of Tic Tac Toe.")
print("This game is meant to be played by 2 human players on the same computer.\n")

start_question = game_starting_message()

while start_question != "Y" and start_question != "N":
    start_question = game_starting_message()

########################################## GAME RUNNING ################################################

if start_question == "N":
    print("Your loss!")

while start_question == "Y":
    game_on = True

    board = [" "] * 10

    player1, player2 = marker_assignment()

    turn = turn_picker()
    print(turn + "will go first!")

    while game_on:

        if turn == "Player 1":

            display_board(board)
            position = player_choice(board)
            placement = marker_placement(board, player1, position)

            if win_condition(board, player1, turn):
                display_board(board)
                print("Congratulations Player 1, you have won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:
            display_board(board)
            position = player_choice(board)
            placement = marker_placement(board, player2, position)

            if win_condition(board, player2, turn):
                display_board(board)
                print("Congratulations Player 2, you have won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"
    if not replay():
        break