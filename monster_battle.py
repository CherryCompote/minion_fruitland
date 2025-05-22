print("Welcome to monster battle! In this game, you try to defeat different monsters with different warriors!")
list_of_warriors = [
    {
    "name": "Gru",
    "hp": 100,
    "attacks": [
        {
            "name": "fart gun",
            "ap": 5,
            "pp": 15
        },
        {
            "name": "kick combo",
            "ap": 10,
            "pp": 5
        }
    ]
    },
]
print("Select your character! Type the character to see the details.")

for warrior in list_of_warriors:
    print(f"- {warrior ["name"]}")

character = input("which character would you like to see the details of?")

character_details = {}

for warrior in list_of_warriors:
    if character == warrior["name"]:
        character_details = warrior

print("Here's the character stats:")
print("-------------")
print(f"Name: {character_details["name"]}")

# TODO Homework:
# 1st homework
# Print the character details nicely so it looks like this
# Name: Gru
# HP: 100
# Attacks:
# - fart gun: attack 5 / can use 15 times
# - kick combo: attack 10 / can use 5 times

# 2nd homework
# and then confirm with the user "Do you want to character or someone else"

# 3rd homework
# add more warriors