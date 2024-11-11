print("Welcome to Cafe House ")

coffee_size =input("Please Provide the coffee size e.g Small, Medium, Large :\n").lower()

extra_shot = input("do yoou want Extra shot Yes/NO :\n").lower()

if extra_shot == "yes":
    coffee = coffee_size + " coffee with an extra shot"
else :
    coffee = coffee_size +" coffee"

print("Order :",coffee)