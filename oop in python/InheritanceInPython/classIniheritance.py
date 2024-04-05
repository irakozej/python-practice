#You have your previously written Parent and Child classes.

# Now, you can create an object of your Child class Football and print the distance variable. 



class Sports:
    type = "Outdoor"
    distance = "short"
    use_hands = False

class Football(Sports):
    name = "Football"
obj = Football()
print(obj.distance)

