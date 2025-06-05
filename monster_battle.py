print("Welcome to monster battle! In this game, you try to defeat different monsters with different warriors!")

list_of_warriors = [
    {
    "name": "Gru",
    "full_name": "Gru",
    "hp": 100, #Hit points
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
    "hp": 90, #Hit points
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
    "name": "George",
    "full_name": "George Lo",
    "hp": 110, #Hit points
    "attacks": [
        {
            "name": "Metal backpack",
            "ap": 15, #Attack power
            "pp": 5, #How many times the player can use it
            "accuracy": 85 #how likely it is to hit the enemy
        },
        {
            "name": "ID swing",
            "ap": 5,
            "pp": 15,
            "accuracy": 90
        }
    ]
    }
]

selected_character = False
user_character = ""

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
    print("Attacks:")
    for attack in character_details["attacks"]:
        print(f"- {attack["name"]}: attack {attack["ap"]} / can use {attack["pp"]} times")

    confirm_character_answer = input("Do you want to use this character or not? (yes/no)")

    if confirm_character_answer == "yes":
        selected_character = True
        user_character = character_details

print(f"Great! You have selected {character_details["name"]}!")
        



# TODO Next Week:
# Random pick opponent
# also add speed to determine who moves first