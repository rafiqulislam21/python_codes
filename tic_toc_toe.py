rowData = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player1 = ""
player2 = ""
gameOver = False
player1Turn = True
playAgain = True
isFirstTime = True


def game_board():
    print("      |   |        ")
    print("  " + rowData[0] + "   | " + rowData[1] + " |   " + rowData[2] + "     ")
    print("------+   +------  ")
    print("  " + rowData[3] + "   | " + rowData[4] + " |   " + rowData[5] + "     ")
    print("------+   +------  ")
    print("  " + rowData[6] + "   | " + rowData[7] + " |   " + rowData[8] + "     ")
    print("      |   |        ")
    print("========================================")


print("Select '*' to press 1 and 'X' to press 2: ")
choice = int(input())
if choice == 1:
    player1 = "*"
    player2 = "X"
elif choice == 2:
    player1 = "X"
    player2 = "*"
print("player 1 selected " + player1)
print("player 2 selected " + player2)


def turn(turnChoice, turnValue):
    if turnChoice == 1:
        if rowData[0] == "1":
            rowData[0] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 2:
        if rowData[1] == "2":
            rowData[1] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 3:
        if rowData[2] == "3":
            rowData[2] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 4:
        if rowData[3] == "4":
            rowData[3] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 5:
        if rowData[4] == "5":
            rowData[4] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 6:
        if rowData[5] == "6":
            rowData[5] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 7:
        if rowData[6] == "7":
            rowData[6] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 8:
        if rowData[7] == "8":
            rowData[7] = turnValue
            return True
        else:
            print("Already used!")
            return False
    elif turnChoice == 9:
        if rowData[8] == "9":
            rowData[8] = turnValue
            return True
        else:
            print("Already used!")
            return False
    else:
        print("Invalid input, please enter 1 to 9.")
        return False


def win_status():
    global gameOver
    if rowData[0] == rowData[1] == rowData[2] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[3] == rowData[4] == rowData[5] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[6] == rowData[7] == rowData[8] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[0] == rowData[3] == rowData[6] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[1] == rowData[4] == rowData[7] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[2] == rowData[5] == rowData[8] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[0] == rowData[4] == rowData[8] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[2] == rowData[4] == rowData[6] == player1:
        print("Player 1 wins")
        gameOver = True
    elif rowData[0] == rowData[1] == rowData[2] == player2:
        print("Player 2 wins")
        gameOver = True
    elif rowData[3] == rowData[4] == rowData[5] == player2:
        print("Player 2 wins")
        gameOver = True
    elif rowData[6] == rowData[7] == rowData[8] == player2:
        print("Player 2 wins")
        gameOver = True
    elif rowData[0] == rowData[3] == rowData[6] == player2:
        print("Player 2 wins")
        gameOver = True
    elif rowData[1] == rowData[4] == rowData[7] == player2:
        print("Player 2 wins")
        gameOver = True
    elif rowData[2] == rowData[5] == rowData[8] == player2:
        print("Player 2 wins")
        gameOver = True
    elif rowData[0] == rowData[4] == rowData[8] == player2:
        print("Player 2 wins")
        gameOver = True
    elif rowData[2] == rowData[4] == rowData[6] == player2:
        print("Player 2 wins")
        gameOver = True
    else:
        pass
        # print("Draw match!")
        # gameOver = True


while playAgain:
    if isFirstTime:
        retry = "y"
    else:
        print("Do you want to play again? press 'y', press 'n' to quit")
        retry = input()
    if retry == "y":
        while not gameOver:
            game_board()
            win_status()
            if gameOver:
                print("Game over")
                break
            if player1Turn:
                print("Player 1's turn: ")
                turnChoice = int(input())
                if turn(turnChoice, player1):
                    player1Turn = False
                else:
                    player1Turn = True
            elif not player1Turn:
                print("Player 2's turn: ")
                turnChoice = int(input())
                if turn(turnChoice, player2):
                    player1Turn = True
                else:
                    player1Turn = False
        # else:
        #     print("Game over")
    elif retry == "n":
        print("Quit game!")
        break
    else:
        print("Invalid input!")
else:
    print("Thanks for playing! You are welcome to play again.")
