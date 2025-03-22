import random

computer = random.choice([-1, 1, 0])
youStr = input("please enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youStr]

print(f"your choice {reverseDict[you]}\nComputer choice {reverseDict[computer]}")

if(computer == you):
    print("It's a tie!")
else:
    if((computer - you == -1) or (computer - you == 2)):
        print("You win!")
    else:
        print("You lose!")

        