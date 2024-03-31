def print_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Get input from the user
n = int(input("Enter an odd integer: "))

# Validate the input
if n % 2 == 0:
    print("Invalid input. Please enter an odd integer.")
elif n < 1 or n >= 1000:
    print("Invalid input. Please enter a number between 1 and 999.")
else:
    # Print the pyramid
    print_pyramid(n)