def sigma(n):
    Sum = 0
    for i in range(1, n + 1):
        Sum = Sum + i
    return Sum

num = int(input("Enter a number: "))
result = sigma(num)
print("The sum of", num, "is", result)

