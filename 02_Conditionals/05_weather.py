weather = input("Provide weather information to suggest the activity : ").lower()

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snow":
    activity ="Build a snowman"

print(activity)
