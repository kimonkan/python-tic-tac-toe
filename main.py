####################################### DEFINING FUNCTIONS ################################################
def gameStartingMessage():
    start_question = input("Do you want to play?(Y/N)").upper()
    return start_question

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
    print("\nPlayer 1 will go first!\n")
    return player1, player2

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

    board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]

    displayBoard(board)
    break
