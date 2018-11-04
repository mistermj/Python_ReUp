'''
multi line comment here says that
this program explains the functions/methods in python
Basically, the __name__ represents the name of the current module
or program that is running. 

It is important to use for the multi-file programs 
'''

def simple_function():
    print("Hello world")

def function():
    simple_function()

if __name__ == "__main__":
    function()
