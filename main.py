print("Hello there! This is a classic game of Tic Tac Toe.")
print("This game was created to be played by 2 human players on the same computer.")

player1 = input("Player 1: Do you want to be X or O?").upper()
player2 = ""
while player1 != "X" and player1 != "O":
    player1 = input("Player 1: Do you want to be X or O? ").upper()
if player1 == "X":
    player2 = "O"
    print("\nPlayer 2 will be O.")
else:
    player2 = "X"
    print("\nPlayer 2 will be X.")
print("\nPlayer 1 will go first!")


