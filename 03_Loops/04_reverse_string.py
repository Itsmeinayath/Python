# Reverse a String
# Problem: Reverse a string using a loop.

input_string = input("Enter the String :\n")

reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string 

print(reversed_string)
