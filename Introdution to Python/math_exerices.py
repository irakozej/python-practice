a = input("enter first number\n")
b = input("enter the second number\n")
c = int(a) + int(b)
if 10 < c < 20:
    print("the sum is  " + str(c) + "and is btn 10 and 20 ")
elif 10 > c:
    print("sum is " + str(c) + " and is less than 10")
elif c > 20:
    print("sum is " + str(c) + " bigger than 20")
