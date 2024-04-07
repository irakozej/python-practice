class Capsule:
    test = True

    ### Add your code below this line ...
    def __init__(self, value1):
        self.__value1 = value1


    ### DO NOT CHANGE BELOW THIS LINE

    def get_value(self):
        return self.__value1

def test_answer(value1):
    obj = Capsule(value1)
    return obj.get_value()