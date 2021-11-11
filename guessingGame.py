import random

randomNum = random.randrange(1,100)
num = -1
while num != randomNum:
    print("Guess a number: ")
    num = int(input())

    if num == randomNum:
        print("Congratulations! You guess correct number")
    elif num > randomNum:
        print("Your guess number is greater than actual number, Try again.")
    elif num < randomNum:
        print("Your guess wrong less than actual number, Try again.")
    else:
        print("Your guess wrong numb, Try again.")

