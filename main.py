############################################ IMPORTING ####################################################
import random

####################################### DEFINING FUNCTIONS ################################################
def gameStartingMessage():
    start_question = input("Do you want to play?(Y/N)").upper()
    return start_question

def turnPicker():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def markerAssignment():
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

def markerPlacement(board, marker, position):
    board[position] = marker

def winCondition(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #across the bottom
    (board[4] == mark and board[5] == mark and board[6] == mark) or #across the middle
    (board[7] == mark and board[8] == mark and board[9] == mark) or #across the top
    (board[1] == mark and board[4] == mark and board[7] == mark) or #across the left
    (board[2] == mark and board[5] == mark and board[8] == mark) or #across the middle
    (board[3] == mark and board[6] == mark and board[9] == mark) or #across the right
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal from bottom left to  top right
    (board[3] == mark and board[5] == mark and board[8] == mark)) #diagonal from top left to  bottom right

def displayBoard(board):
    print("\n" * 100)

    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

########################################## GAME STARTING ################################################
print("\nHello there! This is a classic game of Tic Tac Toe.")
print("This game is meant to be played by 2 human players on the same computer.\n")

start_question = gameStartingMessage()

while start_question != "Y" and start_question != "N":
    start_question = gameStartingMessage()

########################################## GAME RUNNING ################################################
if start_question == "N":
    print("Your loss!")

while start_question == "Y":
    player1, player2 = markerAssignment()

    turn = turnPicker()
    print(turn + "will go first!")

    test_board = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    displayBoard(test_board)
    break
