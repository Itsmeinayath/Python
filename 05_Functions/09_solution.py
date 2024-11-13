def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i
    
for num in even_generator(10):
    print(num)

# What is yield? yield is a keyword that is used like return, except the function will return a generator.
# The generator can be used to iterate over the values one at a time.
# the memory is not allocated for all the values at once, but only for the current value.