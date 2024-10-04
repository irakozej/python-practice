choice = {"celicus": "fahrenheit", "fahrenheit": "celicus"}

user_choice = input("Enter the unit you want to convert from: ")
if user_choice.lower() not in choice:
    print("Invalid choice")
elif user_choice.lower() == "celicus":
    temp = float(input("Enter the temperature in celicus: "))
    temp = (temp * 9/5) + 32
    print(f"The temperature in fahrenheit is: {temp}")
else:    
    temp = float(input("Enter the temperature in fahrenheit: "))
    temp = (temp - 32) * 5/9
    print(f"The temperature in celicus is: {temp}")
    