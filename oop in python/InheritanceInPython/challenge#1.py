### Create a class Animal with an__init__() constructor which takes two arguments; name and sound.

##Then try adding another child class Dog and inherit the Animal class.

## Add a make_sound() method which should print the initial sound variable.


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

class Dog(Animal):
    def make_sound(self):
        print(self.sound)

