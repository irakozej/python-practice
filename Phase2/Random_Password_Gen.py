Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

Symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

import random

print("Welcome to the PyPassword Generator!")
size = int(input("How many letters would you like in your password? between 8 and 20 \n"))
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))

password = []

while size > 8 and size < 20:
    for char in range(1, size + 1):
        password.append(random.choice(Letters))

    for char in range(1, symbols + 1):
        password.append(random.choice(Symbols))

    for char in range(1, numbers + 1):
        password.append(random.choice(Numbers))

    random.shuffle(password)

    password_str = ""
    for char in password:
        password_str += char

    print(f"Your password is: {password_str}")
    break
