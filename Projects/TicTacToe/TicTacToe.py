import time

print('''Welcome to Tic Tac Toe!
The game mechanics are fairly simple similar to a battleship grid.
Choose where you would like to mark your spot by using numbers: 1, 2, 3, 4, 5, 6, 7, 8, or 9.
The locations are marked as below in a 2D array:
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
After you mark your spot the computer will make its move.
Good luck and have fun!\n''')
# global turn
turn = ""
turn2 = ""
choice = input("Would Player 1 like to be X's or O's?")
while turn == "":
    if choice.lower() == "x":
        turn = "X"
        turn2 = "O"
    elif choice.lower() == "o":
        turn = "O"
        turn2 = "X"
    else:
        print("Invalid Syntax. Choose either X's or O's.")
        time.sleep(1.65)
        choice = input("Would you like to be X's or O's?")
        continue
player1 = turn
player2 = turn2
print("\nPlayer 1 will be " + turn + "'s and Player 2 will be " + turn2 + "'s\n")
time.sleep(1.5)

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

board_keys = []

for key in board:
    board_keys.append(key)


def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])


def main():
    global turn
    global player1
    global player2
    count = 0

    for i in range(10):
        printBoard(board)
        print("It is your turn. Where would you like to place " + turn + " at?")
        move = int(input())
        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("Uh oh. That spot is filled already.\nWhere would you like to place " + turn + " at?")
            continue

        if count >= 5:
            # Top Row
            if (board[1] == "X") and (board[2] == "X") and (board[3] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[1] == "O") and (board[2] == "O") and (board[3] == "O"):
                printBoard(board)
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            # Middle Row
            elif (board[4] == "X") and (board[5] == "X") and (board[6] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[4] == "O") and (board[5] == "O") and (board[6] == "O"):
                printBoard(board)
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            # Bottom Row
            elif (board[7] == "X") and (board[8] == "X") and (board[9] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[7] == "O") and (board[8] == "O") and (board[9] == "O"):
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            # Left Side
            if (board[1] == "X") and (board[4] == "X") and (board[7] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[1] == "O") and (board[4] == "O") and (board[7] == "O"):
                printBoard(board)
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break

            # Middle Side
            elif (board[2] == "X") and (board[5] == "X") and (board[8] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[2] == "O") and (board[5] == "O") and (board[8] == "O"):
                printBoard(board)
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break

            # Right Side
            elif (board[3] == "X") and (board[6] == "X") and (board[9] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[3] == "O") and (board[6] == "O") and (board[9] == "O"):
                printBoard(board)
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break

            # Left Hoizontal "/"
            elif (board[3] == "X") and (board[5] == "X") and (board[7] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[3] == "O") and (board[5] == "O") and (board[7] == "O"):
                printBoard(board)
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break

            # Right Horizontal "\"
            elif (board[1] == "X") and (board[5] == "X") and (board[9] == "X"):
                printBoard(board)
                if player1 == "X":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break
            elif (board[1] == "O") and (board[5] == "O") and (board[9] == "O"):
                printBoard(board)
                if player1 == "O":
                    print("Player 1 has won!")
                    break
                else:
                    print("Player 2 has won!")
                    break

        if count == 9:
            print("DRAW!")
            break

        if turn == "O":
            turn = "X"
        else:
            turn = "O"
    time.sleep(.85)
    reset = input("Do you want to play again? (y/n)")
    if reset.lower() == "y":
        for key in board_keys:
            board[key] = " "

        main()
    else:
        print("Thanks for playing!")

main()
