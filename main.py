name = input("What is your minion name?")
experience_level = int(input("What is your experience level?"))
mission_num = int(input("What is your mission number?"))
failed_mission = False

print(f"Hi {name}! Your experience level is {experience_level}, and your mission number today is {mission_num}.")

supplies = {
    "fartgun": 2,
    "lip_balm": 1,
    "banana": 13,
    "water_bottle": 0
}

print("Your current supplies are ")
print(supplies)

continue_adding_supplies = True

while continue_adding_supplies:

    add_supplies = input("Do you want to add more supplies?")

    if add_supplies == "yes":
        supply_name = input("What is the supply's name?")
        supply_num = int(input("How many?"))

        if supply_name in supplies:
            supplies[supply_name] += supply_num
            # first one is adding 2 to itself
        else:
            supplies[supply_name] = supply_num
            # second one is setting itself to 2

    else:
        continue_adding_supplies = False

print("Your updated supplies are ")
print(supplies)


# places = ["banana village", "kiwi forest", "pineapple mountain"]

# for place in places:
#     print(f"- {place}")

# choice = input("Do you want to add more fruitlands?")
# if choice == "yes" :
#     new_place = input("What is it's name? ")
#     places.append(new_place)

# choice = input("Do you want to remove any fruitlands?")
# if choice == "yes" :
#     rmv_place = input("Which one? ")
#     places.remove(rmv_place)


# print("This is the new list:")
# for place in places:
#     print(f"- {place}")

# if mission_num > 0 and mission_num <= 25:
#     print("This is an easy mission.")
# elif mission_num > 25 and mission_num <= 50:
#     print("This is a normal mission.")
# elif mission_num > 50 and mission_num <= 75:
#     print("This is a hard mission!")
# else:
#     print("Whew! This is a EXTREME mission!")

destination = input("Where do you want to explore?")

if destination == "banana village":

    print("Okay! Get ready for banana cream pies!")
    experience_level += 10

    print("Because you came to banana village, your minions took 5 bananas but you lost 2 water bottles due to the bananas being sweet.")
    if "water_bottle" in supplies:
        supplies["water_bottle"] -= 2 
        if supplies["water_bottle"] < 0:
            failed_mission = True
    else:
        failed_mission = True
    
    if "banana" in supplies:
        supplies["banana"]+= 5
    else:
        supplies["banana"] = 5

elif destination == "kiwi forest":
    print("Ooo! Get ready for Kiwi bird attacks!")
    experience_level += 20

    print("Because you came to kiwi forest, you used a pair of gloves for touching the kiwis, but you got 10 kiwis.")
    if "gloves" in supplies:
        supplies["gloves"] -= 2
        if supplies["gloves"] < 0:
            failed_mission = True
    else:
        failed_mission = True

    if "kiwi" in supplies:
        supplies["kiwi"]+= 10
    else:
        supplies["kiwi"] = 10


elif destination == "pineapple mountain":
    print("Yikes! Get ready to meet the pineapple cave monster!")
    experience_level += 30

    # TODO: add supply changes

else:
    print("Uh oh! This location isn't in our maps, be careful!")
    experience_level += 50

    # TODO: add supply changes


if failed_mission:
    print("Uh oh! You failed the mission because you ran out of supplies!}")
    print("The supply that ran out was:")
    for key, value in supplies.items():
        if value < 0 :
            print(key)
else:    
    print(f"Woohoo! You finished your mission! Your new experience level is {experience_level}")
    print("Remaining supples:")
    print(supplies)


# cartoons = {
#     "Minions": "Gru",
#     "Mickey and Friends": "Goofy",
#     "Tom & Jerry": "Jerry"
# }

# for ke, valu in cartoons.items():
#     print(f"{ke} = = = = = {valu}")

# for key in cartoons:
#     print(f"{key} = = = = = {cartoons[key]}")