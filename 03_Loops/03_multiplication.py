#  Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter the number : \n"))

for i in range(1,11):
    if i == 5:
        continue
    print(f"{num} x {i} = {num*i}")