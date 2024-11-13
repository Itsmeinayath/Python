#scope in python is the region where a variable is recognized.
#There are mainly two types of scope:
#1. Global scope
#2. Local scope
# *****************************************************
#3. Enclosed scope
#4. Built-in scope

#Global scope: A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.

# The global scope values can be accessed from anywhere in the code. in any function or any block of code.
# The local scope values can be accessed only from the block of code where it is defined.





#Example:
x = 300
def myfunc():
    print(x)
myfunc()
print(x)

#Local scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
#Example:
def myfunc():
    y = 300
    print(y)
myfunc()
#print(y) #This will cause an error because the variable y is not available outside the function.

#Function Inside Function: As explained in the example above, the variable y is not available outside the function, but it is available for any function inside the function.
