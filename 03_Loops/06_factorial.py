num = int(input("Enter the number :\n"))
num_org = num
factorial = 1
while num > 0:
    factorial = factorial * num
    num = num -1
print("Factorial of",num_org,"is : ",factorial)