#Create a class Sports with a class variable, outdoor = True, and an __init__() method which takes two parameters, sports name and sports team, and save these values to the self variables with the names sports_name and sports_team accordingly.

class Sports:
    outdoor = True
    def __init__(self, name, team):
        self.sports_name = name
        self.sports_team = team
