fruit = input("Enter the Fruite :").lower()
color = input("Enter the Fruit condition e.g Green, Yellow, Brown: ").lower()

if fruit :
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("OverRipe") 

# else:
#     print("The Fruit is not Banana")