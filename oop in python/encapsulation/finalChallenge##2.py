# Write your class here ...
class System:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def login(self, user, passw):
        if user == self.__username and passw == self.__password:
            print("Login Successful")
        
        else:
            print("Invalid Credentials")




### Don't change below this line

def test_answer(username, password, user, passw):
        obj = System(username, password)
        obj.login(user, passw)
