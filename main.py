RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"


print(LIGHT_WHITE)

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

places = ["banana village", "kiwi forest", "watermelon mountain"]

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


finished_exploring = False

while finished_exploring == False:

    print(LIGHT_WHITE)
    destination = input("Where do you want to explore?")

    if destination == "banana village":

        print(YELLOW)

        print("Okay! Get ready for banana cream pies!")
        experience_level += 10

        print("Because you came to banana village, your minions took 5 bananas but you lost 3 water bottles due to the bananas being sweet.")

        if "water_bottle" not in supplies:
            supplies["water_bottle"] = 0

        supplies["water_bottle"] -= 3

        if "banana" not in supplies:
            supplies["banana"] = 0

        supplies["banana"] += 5

    elif destination == "kiwi forest":

        print(GREEN)

        print("Ooo! Get ready for Kiwi bird attacks!")
        experience_level += 20

        print("Because you came to kiwi forest, you used a pair of gloves for touching the kiwis, but you got 10 kiwis.")

        if "gloves" not in supplies:
            supplies["gloves"] = 0

        supplies["gloves"] -= 2

        if "kiwi" not in supplies:
            supplies["kiwi"] = 0

        supplies["kiwi"] += 10

    elif destination == "watermelon mountain":

        print(LIGHT_RED)

        print("Yikes! Get ready to meet the watermelon cave monster!")
        experience_level += 30

        print("Because you came to watermelon mountain, you used one sword to fight the monster, but you got 1 watermelon.")

        # sword changes
        if "sword" not in supplies:
            supplies["sword"] = 0

        supplies["sword"] -= 1

        if "watermelon" in supplies:
            supplies["watermelon"]+= 1
        else:
            supplies["watermelon"] = 1

    else:
        print("Uh oh! This location isn't in our maps, be careful!")
        experience_level += 50

        # TODO: add supply changes


    print(LIGHT_WHITE)
    finished_exploring_answer = input("Are you done exploring?")

    if finished_exploring_answer == "yes":
        finished_exploring = True


# Evaluate failed mission
for key in supplies:
    if supplies[key] < 0:
        failed_mission = True


if failed_mission:
    print(RED)
    print("Uh oh! You failed the mission because you ran out of supplies!}")
    print("The supply that ran out was:")
    for key, value in supplies.items():
        if value < 0 :
            print(key)
else:    
    print(CYAN)
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