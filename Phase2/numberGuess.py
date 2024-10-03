import random


print("We have generated a random number, your task is to guess untill you found it or you are out of trials.")
num = input("Enter a number: \n")

a = random.randint(1, 10)

trials = 0
while trials < 5:
    if int(num) == a: 
        print("congrats, you have found the number")
        break
    else: 
        if int(num )< a:
            print("The number is greater than that")
        else:
            print("The number is less than that")
    num = input("Enter a number: ")
    trials += 1