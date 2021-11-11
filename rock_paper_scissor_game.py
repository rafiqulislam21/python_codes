import random

yourChoice = 0
print("Any time to quit game press '-1'")

while yourChoice != -1:
    print("'rock' = 1, 'paper' = 2, 'scissor' = 3 ")
    computerChoice = int(random.randrange(1,3))
    yourChoice = int(input())

    computerChoiceName = ''
    yourChoiceName = ''
    if computerChoice == 1:
        computerChoiceName = "rock"
    elif computerChoice == 2:
        computerChoiceName = "paper"
    elif computerChoice == 3:
        computerChoiceName = "scissor"
    else:
        computerChoiceName = "Invalid choice"

    if yourChoice == 1:
        yourChoiceName = "rock"
    elif yourChoice == 2:
        yourChoiceName = "paper"
    elif yourChoice == 3:
        yourChoiceName = "scissor"
    else:
        computerChoiceName = "Invalid choice"

    print("Computer's choice: "+computerChoiceName)
    print("Your choice: "+yourChoiceName)

    if yourChoice > 3 or yourChoice < 1:
        print('Not valid choice')
    else:
        if (computerChoice == 1 and yourChoice == 1) or (computerChoice == 2 and yourChoice == 2) or (
                computerChoice == 3 and yourChoice == 3):
            print("Draw, Try again.")
        else:
            if computerChoice == 1 and yourChoice == 2:
                print("Congratulation! You won")
            else:
                if computerChoice == 1 and yourChoice == 3:
                    print("Computer won, Better luck next time.")
                else:
                    if computerChoice == 2 and yourChoice == 3:
                        print("Congratulation! You won.")
                    else:
                        print("Computer won, Better luck next time.")
