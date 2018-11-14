class RandomClass:
    __some_var = ""

    def __init__(self, name):
        self.__some_var = name

Object = RandomClass("dadoo")
Object.__some_var