def f1():
    x = 88
    def f2():
        print(x)
    return f2

result = f1()
result()

# Here the return f2 returns the inner function memory refere and the variable which are used in the inner function.
# the variable can from the outer function or the global variable. so the output will be 88.
# This is called closure. the inner function is accessing the variable of the outer function.

