age = int(input("Provide the age :\n "))
is_wednesday = input("Is it wednesday ? (yes/no):").strip().lower() == "yes"
price = 12 if age >= 18 else 8

if is_wednesday :
    # price = price-2
    price -=2

print("Ticket price for you is $",price)