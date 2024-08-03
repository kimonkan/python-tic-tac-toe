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
    print("\nPlayer 1 will go first!")
    return player1, player2

def displayBoard(board):
    pass

########################################## GAME STARTING ################################################
print("\nHello there! This is a classic game of Tic Tac Toe.")
print("This game is meant to be played by 2 human players on the same computer.\n")

start_question = gameStartingMessage()

while start_question != "Y" and start_question != "N":
    start_question = gameStartingMessage()

########################################## GAME RUNNING ################################################
while start_question == "Y":
    player1, player2 = markerAssignment()
    break

if start_question == "N":
    print("Your loss!")