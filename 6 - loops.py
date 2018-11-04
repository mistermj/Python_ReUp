# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
'''
unlike languages like C,CPP.. we can use else for loops. 
When the loop condition of "for" or "while" statement fails then 
code part in "else" is executed. 
If break statement is executed inside for loop then 
the "else" part is skipped. Note that "else" part is executed 
even if there is a continue statement.
'''
