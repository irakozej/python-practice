a_string = input("Enter a string: ")
def adversarial_color(a_string):
    
    new_string = a_string.replace("red", "green")
    new_string = new_string.replace("blue", "green")
    
    print(new_string)