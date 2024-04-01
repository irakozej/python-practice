# Create a method print_info(), which will print all the above details in this order:

# If sports_name is Golf and sports_team is America, the output should be:

# Golf - America

# And if not then the output is: -



class Sports:
    outdoor = True
    def __init__(self, name, team):
        self.sports_name = name
        self.sports_team = team
    def print_info(self):
        print(f"{self.sports_name} - {self.sports_team}")