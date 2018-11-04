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

def function_with_args (first = "M.", second = "Anon"):
    print(f'The name is {first, second}')

def main():
    function_with_args("Mr.", "Dadoo")
    print(function_with_args)# prints objects
    
if __name__ == "__main__":
    main()
