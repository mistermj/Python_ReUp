'''
weird behavior of variables in python.

'''

value = 7 # it's an integer value. Python knows it
value = "somevalue" # now, it changes that to string. 
# so not like C++/Java Or C#

# Declare a global and local scope variable


def main():
    global value
    value = "something just like this"
    print(f"it will print {value}")

if __name__ == '__main__':
    main()

print(value) # prints the global var declared in function.