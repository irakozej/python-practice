def print_pyramid(n):
    # Loop through each row
    for i in range(n//2 + 1):
        # Print leading spaces
        # for j in range(n//2 - i):
        #     print(" ", end=" ")
        
        # Print asterisks
        space = (n- i*2)//2 * ' '
        for k in range(2 * i + 1):
            asterick = "*"
            # print(space + "*" + space)
        print(space + (k+1)*asterick + space)
        # Move to the next line

# Get user input for the number of rows in the pyramid
n = int(input())
if n % 2 != 0:
    print_pyramid(n)
else:
    print("Enter an odd number.")