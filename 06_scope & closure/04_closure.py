def code(num):
    def actual(x):
        return x ** num
    return actual

square = code(2)
cube = code(3)

print(square(5))
print(cube(5))

# Here is break down of the code:

# The code() function takes a number as an argument and returns the actual() function.
# The actual() function takes a number as an argument and returns the square of the number.
# The code() function is called with the argument 2. The square() function is returned.
# The square() function is called with the argument 5. The square of 5 is 25.
# The code() function is called with the argument 3. The cube() function is returned.
# The cube() function is called with the argument 5. The cube of 5 is 125.
# The code() function is a closure because it captures the num argument of the code() function.
    