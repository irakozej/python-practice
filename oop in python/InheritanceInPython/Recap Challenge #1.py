# Create a Parent class, Plant with an __init__() constructor and two arguments on it: scientific_name and climate.

# Finally, create a Child class, Lotus, and inherit the parent class.

class Plant:
    def __init__(self, scientific_name, climate):
        self.scientific_name = scientific_name
        self.climate = climate

class Lotus(Plant):
    pass

