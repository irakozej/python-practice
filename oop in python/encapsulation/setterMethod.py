class Capsule:
    test = True

    def __init__(self, value1):
        self.__value1 = value1
    
    def get_value(self):
        return self.__value1

    ### Add your code below this line...
    def set_value(self,new_val):
        self.__value1 = new_val



### DO NOT CHANGE BELOW THIS LINE

def test_answer(value1, new_val):
    obj = Capsule(value1)
    obj.set_value(new_val)
    return obj.get_value()