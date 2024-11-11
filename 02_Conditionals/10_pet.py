pet = input("Provide the pet (e.g : Dog, Cat)\n").lower()
age = int(input("Provide the age of the pet : \n"))


if pet == "dog":
    if age < 2 :
        food = "puppy food"
    elif age > 5:
        food ="Adult dog food"
    else:
        food="Senior dog food"

elif pet == "cat":
    if age < 2 :
        food = "puppy food"
    elif age > 5:
        food ="Adult cat food"
    else:
        food="Senior cat food"
print("Ai recomendation is : ",food)
