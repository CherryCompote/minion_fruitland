import random

print("Welcome to monster battle! In this game, you try to defeat other warriors!")

list_of_warriors = [
    {
    "name": "Gru",
    "full_name": "Gru",
    "speed": 70,
    "hp": 100, #Health points
    "attacks": [
        {
            "name": "fart gun",
            "ap": 5, #Attack power
            "pp": 15, #How many times the player can use it
            "accuracy": 95 #how likely it is to hit the enemy
        },
        {
            "name": "kick combo",
            "ap": 10,
            "pp": 5,
            "accuracy": 80
        }
    ]
    },
    {
    "name": "Bob",
    "full_name": "Bob the Minion",
    "speed": 90,
    "hp": 90, #Health points
    "attacks": [
        {
            "name": "laser gun",
            "ap": 10, #Attack power
            "pp": 10, #How many times the player can use it
            "accuracy": 90 #how likely it is to hit the enemy
        },
        {
            "name": "rocket",
            "ap": 50,
            "pp": 2,
            "accuracy": 50
        }
    ]
    },
    {
    "name": "Taylor",
    "full_name": "Taylor Swift",
    "speed": 80,
    "hp": 110, #Health points
    "attacks": [
        {
            "name": "mic throw",
            "ap": 20, #Attack power
            "pp": 5, #How many times the player can use it
            "accuracy": 75 #how likely it is to hit the enemy
        },
        {
            "name": "magic song",
            "ap": 10,
            "pp": 10,
            "accuracy": 85
        }
    ]
    },
    {
    "name": "Mario",
    "full_name": "Mario",
    "speed": 85,
    "hp": 100, #Health points
    "attacks": [
        {
            "name": "fireball",
            "ap": 10, #Attack power
            "pp": 10, #How many times the player can use it
            "accuracy": 90 #how likely it is to hit the enemy
        },
        {
            "name": "up punch",
            "ap": 15,
            "pp": 5,
            "accuracy": 75
        }
    ]
    },
    {
    "name": "Peach",
    "full_name": "Princess Peach",
    "speed": 60,
    "hp": 120, #Health points
    "attacks": [
        {
            "name": "toad attack",
            "ap": 10, #Attack power
            "pp": 5, #How many times the player can use it
            "accuracy": 95 #how likely it is to hit the enemy
        },
        {
            "name": "umbrella wack",
            "ap": 20,
            "pp": 8,
            "accuracy": 75
        }
    ]
    },
    {
    "name": "George",
    "full_name": "George Lo",
    "speed": 80,
    "hp": 110, #Health points
    "attacks": [
        {
            "name": "metal backpack",
            "ap": 15, #Attack power
            "pp": 5, #How many times the player can use it
            "accuracy": 85 #how likely it is to hit the enemy
        },
        {
            "name": "id swing",
            "ap": 5,
            "pp": 15,
            "accuracy": 90
        }
    ]
    },
    {
    "name": "Mickey",
    "full_name": "Mickey Mouse",
    "speed": 80,
    "hp": 90, #Health points
    "attacks": [
        {
            "name": "toodles",
            "ap": 5, #Attack power
            "pp": 15, #How many times the player can use it
            "accuracy": 90 #how likely it is to hit the enemy
        },
        {
            "name": "sorceror blast",
            "ap": 20,
            "pp": 5,
            "accuracy": 75
        }
    ]
    },
    {
    "name": "Minnie",
    "full_name": "Minnie Mouse",
    "speed": 75,
    "hp": 90, #Health points
    "attacks": [
        {
            "name": "toodles",
            "ap": 5, #Attack power
            "pp": 15, #How many times the player can use it
            "accuracy": 90 #how likely it is to hit the enemy
        },
        {
            "name": "bow throw",
            "ap": 15,
            "pp": 8,
            "accuracy": 80
        }
    ]
    },
    {
    "name": "Harry",
    "full_name": "Harry Potter",
    "speed": 90,
    "hp": 90, #Health points
    "attacks": [
        {
            "name": "avada kedavra",
            "ap": 30, #Attack power
            "pp": 1, #How many times the player can use it
            "accuracy": 95 #how likely it is to hit the enemy
        },
        {
            "name": "stupefy",
            "ap": 5,
            "pp": 10,
            "accuracy": 80
        }
    ]
    },
    {
    "name": "Cleopatra",
    "full_name": "Cleopatra",
    "speed": 80,
    "hp": 120, #Health points
    "attacks": [
        {
            "name": "sandstorm",
            "ap": 15, #Attack power
            "pp": 5, #How many times the player can use it
            "accuracy": 90 #how likely it is to hit the enemy
        },
        {
            "name": "poison dart",
            "ap": 10,
            "pp": 10,
            "accuracy": 85
        }
    ]
    }
]

selected_character = False
user_character = {}

while not selected_character: #also can type: while selected_character == False:
    print("Select your character! Type the character to see the details.")

    for warrior in list_of_warriors:
        print(f"- {warrior ["full_name"]}")

    character = input("which character would you like to see the details of?")

    character_details = {}

    for warrior in list_of_warriors:
        # Check if the user input is equal to either the name or full name
        # comparing it to lowercase
        if character.lower() == warrior["name"].lower() or character.lower() == warrior["full_name"].lower():
            character_details = warrior

    print("Here's the character stats:")
    print("-------------")
    print(f"Name: {character_details["full_name"]}")
    print(f"HP: {character_details["hp"]}")
    print(f"Speed: {character_details["speed"]}")
    print("Attacks:")
    for attack in character_details["attacks"]:
        print(f"- {attack["name"]}: attack {attack["ap"]} / can use {attack["pp"]} times")

    confirm_character_answer = input("Do you want to use this character or not? (yes/no)")

    if confirm_character_answer == "yes":
        selected_character = True
        user_character = character_details

print(f"Great! You have selected {character_details["name"]}!")
        
selected_opponent = False
opponent_character = {}

while not selected_opponent:
    opponent_character = random.choice(list_of_warriors)
    if opponent_character["name"] != user_character["name"]:
        selected_opponent = True

print(f"Your challenger is {opponent_character["name"]}. Get ready to fight!")
print("============================")
print(f"Beginning battle between {user_character["name"]} and {opponent_character["name"]}!")

turns = 0

while user_character["hp"] > 0 and opponent_character["hp"] > 0:
    turns += 1
    print(f"This is turn number #{turns}")
    print(f"{user_character["name"]} HP : {user_character["hp"]}")
    print(f"{opponent_character["name"]} HP : {opponent_character["hp"]}")

    print("Which attack do you want to use?")
    for index, attack in enumerate(user_character["attacks"]):
        print(f"{index+1}. {attack["name"].upper()}")
        print(f"- Attack power: {attack["ap"]}")
        print(f"- Remaining usage: {attack["pp"]}")
        print(f"- Accuracy: {attack["accuracy"]}")
    print("Enter the number")
    attack_choice = int(input(""))-1

    opponent_number_of_attacks = len(opponent_character["attacks"])
    opponent_attack_choice = random.randint(0, opponent_number_of_attacks - 1)

    user_attack = user_character["attacks"][attack_choice]
    opponent_attack = opponent_character["attacks"][opponent_attack_choice]
    if user_character["speed"] >= opponent_character["speed"]:
        print("==============")
        print(" ")
        print(f"{user_character["name"]} used {user_attack["name"].upper()}!")
        print(f"{opponent_character["name"]} lost {user_attack["ap"]} HP")
        print(" ")
        opponent_character["hp"] -= user_attack["ap"]
        user_attack["pp"] -= 1

        if opponent_character["hp"] <= 0:
            break

        print(f"{opponent_character["name"]} used {opponent_attack["name"].upper()}!")
        print(f"{user_character["name"]} lost {opponent_attack["ap"]} HP")
        user_character["hp"] -= opponent_attack["ap"]
        opponent_attack["pp"] -= 1
        print(" ")
        print(" ")
        print("=============")

        if user_character["hp"] <= 0:
            break
    else:
        print("==============")
        print(" ")
        print(f"{opponent_character["name"]} used {opponent_attack["name"].upper()}!")
        print(f"{user_character["name"]} lost {opponent_attack["ap"]} HP")
        user_character["hp"] -= opponent_attack["ap"]
        opponent_attack["pp"] -= 1

        if user_character["hp"] <= 0:
            break
        print(f"{user_character["name"]} used {user_attack["name"].upper()}!")
        print(f"{opponent_character["name"]} lost {user_attack["ap"]} HP")
        print(" ")
        opponent_character["hp"] -= user_attack["ap"]
        user_attack["pp"] -= 1
        print(" ")
        print(" ")
        print("=============")
        if opponent_character["hp"] <= 0:
            break



if user_character["hp"] <= 0 :
    print(f"Uh oh, {user_character["name"]} lost... You can always try again.")
elif opponent_character["hp"] <= 0 :
    print(f"Yay, You win! You defeated {opponent_character["name"]}!")

    
# TODO Next Week:
# Random pick opponent
# also add speed to determine who moves first.