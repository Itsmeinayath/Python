# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.


num = int(input("Enter the number :\n"))
sum = 0

for i in range(1, num+1):
    if i % 2 == 0:
        sum += 1

print("The sum of even number is :",sum)