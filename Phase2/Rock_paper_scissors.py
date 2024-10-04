choice = {"Rock", "Paper", "Scissors"}
import random

print("Welcome to Rock, Paper, Scissors game")
print("You have to play with the computer")
print("Enter your choice: Rock, Paper or Scissors")
user = input("Enter your choice: ")
computer = random.choice(["Rock", "Paper", "Scissors"])

print(f"Computer choice is: {computer}")

if user == computer:
    print("It's a tie")
elif user == "Rock":
    if computer == "paper":
        print("computer wins")
    else:
        print("You win")
elif user == "Paper":
    if computer == "scissors":
        print("computer wins")
    else:
        print("You win")
elif user == "Scissors":
    if computer == "rock":
        print("computer wins")
    else:
        print("You win")
else:
    print("Invalid choice")

