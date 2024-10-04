choice = {"Rock", "Paper", "Scissors"}
import random

print("Welcome to Rock, Paper, Scissors game")
print("You have to play with the computer")
print("Enter your choice: Rock, Paper or Scissors")
user = input("Enter your choice: ")
computer = random.choice(list(choice))

print(f"Computer choice is: {computer}")

while True:
    if user == computer:
        print("It's a tie")
        break
    elif user == "Rock":
        if computer == "Paper":
            print("computer wins")
        else:
            print("You win")
    elif user == "Paper":
        if computer == "Scissors":
            print("computer wins")
        else:
            print("You win")
    elif user == "Scissors":
        if computer == "Rock":
            print("computer wins")
        else:
            print("You win")
    else:
        print("Invalid choice")

    break
