distance = int(input("Enter the distance : "))

if distance < 3:
    transport = "By walk"
elif distance <= 15 :
    transport ="Via Bike"
else :
    transport = "Via car"

print("Transportation mode is :",transport)