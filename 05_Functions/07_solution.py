def sum_all(*args):
   return sum(args)

print(sum_all(1, 2, 3, 4, 5))  
print(sum_all(1, 2, 3, 4, 5, 6))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

# Here we are using the *args parameter to pass a variable number of arguments to the function.it allows multiple arguments to be passed to the function.
# The *args parameter is used when we are unsure about the number of arguments that will be passed to the function.
# The name its self defines that it is an argument, and the asterisk (*) defines that it can take multiple arguments.
# The sum() function returns the sum of all the arguments passed to it. its a built-in function in Python.
