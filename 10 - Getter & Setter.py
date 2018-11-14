class Information:

    _name = ""
    _age = 0

    def __init(self, name, age):
        self._name = name
        self._age = age

    #getter
    def get_name(self):
        return self._name.upper()
    
    # setter
    def set_name(self, value):
        self._name = value + "someone changed the value"

    def get_intro(self):
        return "information_name is {}".format(self.get_name)

handle = Information()
handle.set_name("meindak")

print(handle.get_intro())

#=====================================#
'''
getter and setter in C# or other strict languages is rather a property
when we set or get some information, we are essentially invoking a method call.
we are not assigning values to properties. we need to make these into properties
'''

