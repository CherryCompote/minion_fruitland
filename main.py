name = input("What is your minion name?")
experience_level = int(input("What is your experience level?"))
mission_num = int(input("What is your mission number?"))

print(f"Hi {name}! Your experience level is {experience_level}, and your mission number today is {mission_num}.")

places = ["banana village", "kiwi forest", "pineapple mountain"]

for place in places:
    print(f"- {place}")

choice = input("Do you want to add more fruitlands?")
if choice == "yes" :
    new_place = input("What is it's name? ")
    places.append(new_place)

choice = input("Do you want to remove any fruitlands?")
if choice == "yes" :
    rmv_place = input("Which one? ")
    places.remove(rmv_place)


print("This is the new list:")
for place in places:
    print(f"- {place}")

if mission_num > 0 and mission_num <= 25:
    print("This is an easy mission.")
elif mission_num > 25 and mission_num <= 50:
    print("This is a normal mission.")
elif mission_num > 50 and mission_num <= 75:
    print("This is a hard mission!")
else:
    print("Whew! This is a EXTREME mission!")

destination = input("Where do you want to explore?")

if destination == "banana village":
    print("Okay! Get ready for banana cream pies!")
    experience_level += 10
elif destination == "kiwi forest":
    print("Ooo! Get ready for Kiwi bird attacks!")
    experience_level += 20
elif destination == "pineapple mountain":
    print("Yikes! Get ready to meet the pineapple cave monster!")
    experience_level += 30
else:
    print("Uh oh! This location isn't in our maps, be careful!")
    experience_level += 50
