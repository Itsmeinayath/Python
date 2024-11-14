

# username = "Inayth"

# def func():
#     username = "Moahmmed"
#     print(username)

# print(username)
# func()

# Here is break down of the code:
# The variable username is a global variable. which holds the value "Inayath".
# The variable username is a local variable of the func() function. which holds the value "Mohammed".
# The print() function prints the global username variable. which holds the value "Inayath".
# The print() function prints the local username variable. which holds the value "Mohammed".

# username = "Inayth"
# def func():
#     print(username)

# print(username)
# func()

# Here in the above code the username variable is a global variable. which holds the value "Inayath".
#  in the function we are using the usernsme which is a global variable. so the output will be "Inayath".
# The print() function prints the global username variable. which holds the value "Inayath".

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# ********************************************************************************************************************

# def func3():
#     # This is bad practice to manupulate the global variable.
#     global x # This will make the x variable global. it will manupulate the global variable. now the value will be changed
#     x = 88
# func3()
# print(x)

def f1():
        x = 88
        def f2():
            print(x)
        f2()

f1()

# Here function contains another function. the inner function is accessing the variable of the outer function.
# The inner function is accessing the variable x of the outer function. so the output
# if we dont have the x variable in the inner function then it will look for the outer function. if it is not there then it will look for the global variable.
 