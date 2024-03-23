a = float(input("enter first number\n"))
c = input("enter a sign\n")
b = float(input("enter a second number\n"))
ans = a+b
if c == "+":
    print(f"The answer is: {ans}")

elif c == "-":
     print(f"The answer is: {ans}")

elif c == "*":
     print(f"The answer is: {ans}")

elif c == "/":
     print(f"The answer is: {ans}")

else:
    print("enter valid number and operator")
