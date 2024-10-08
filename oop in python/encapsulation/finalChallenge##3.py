# Write your class here ...
class Numbers:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

class Calculator(Numbers):
    def add(self):
        return self.value1 + self.value2
    
    def multiply(self):
        return self.value1 * self.value2

    def subtract(self):
        return self.value1 - self.value2    





### Do not change below this line

def test_answer(num1, num2):
    num1 = input("enter a first number: ")
    num2 = input("enter a second number: ")
    obj = Calculator(num1, num2)
    return obj.add(), obj.multiply(), obj.subtract()
