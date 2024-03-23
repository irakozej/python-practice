iterations = int(input("enter number of iterations: \n"))
num1 = int(input("enter a number: \n"))
num2 = int(input("enter another number: \n"))

def bigger(arg1, arg2):
    if arg1 >= arg2:
        print(arg1)
    else:
        print(arg2)
    

for i in range(iterations):
    variable = bigger(num1, num2)
    
    new_value = variable / 2
    if num1 >= num2:
        num1 = new_value
        print(num1)
    else:
        num2 = new_value
        print(num2)
    


    