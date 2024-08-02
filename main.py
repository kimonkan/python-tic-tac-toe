print("Hello there! This is a classic game of Tic Tac Toe.")
print("This game was created to be played by 2 human players on the same computer.")

player1 = input("Player 1: Do you want to be X or O?")
player2 = ""
while player1 != "X" or player1 != "O":
    player1 = input("Player 1: Do you want to be X or O?")
if player1 == "X":
    player2 == "O"
    print("2 O")
else:
    player2 == "X"
    print("2 X")
print("Player 1 will go first!")


