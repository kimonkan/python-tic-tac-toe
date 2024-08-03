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

def initializeBoard():
    return [[" " for _ in range(3)] for _ in range(3)]

def displayBoard(board):
    for row in board:
        print("|".join(row))
        print("-" * 5) #Separator line between rows

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

    board = initializeBoard()
    displayBoard(board)
    break
