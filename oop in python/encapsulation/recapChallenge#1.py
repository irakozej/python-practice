# Add Your Code Here...
class Login:
    def __init__(self, username,password):
        self.__username = username
        self.__password = password
    
    def see_credentials(self):
        return (self.__username, self.__password)


### DO NOT CHANGE BELOW THIS LINE

def test_answer(username, password):
    obj = Login(username, password)
    return obj.see_credentials()