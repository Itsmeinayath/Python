def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name = "Ironman", power = "suit")
print_kwargs(name = "Thor", power = "hammer",enemy = "Loki")
print_kwargs(name = "Groot", power = "I am Groot", enemy = "Thanos", friend = "Rocket")

# Here we are using **kwargs to pass multiple keyword arguments to the function.
# The function then iterates over the dictionary and prints the key-value pairs.
# The double asterisk (**) is used to pass keyword arguments to the function. 
# we have to use loop to iterate over the dictionary and print the key-value pairs.