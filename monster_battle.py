import random
from warriors import full_list_of_warriors
from formatting import space, line, space_line


list_of_warriors = full_list_of_warriors

selected_character = False
user_character = {}

while not selected_character: #also can type: while selected_character == False:
    space_line()
    print("Select your character! Type the character to see the details.")
    space_line()

    for warrior in list_of_warriors:
        print(f"- {warrior ["full_name"]}")
        space()

    character = input("Which character would you like to see the details of?")

    character_details = {}

    for warrior in list_of_warriors:
        # Check if the user input is equal to either the name or full name
        # comparing it to lowercase
        if character.lower() == warrior["name"].lower() or character.lower() == warrior["full_name"].lower():
            character_details = warrior
    space()
    print("Here's the character stats:")
    line()
    print(f"Name: {character_details["full_name"]}")
    print(f"HP: {character_details["hp"]}")
    print(f"Speed: {character_details["speed"]}")
    print("Attacks:")
    for attack in character_details["attacks"]:
        print(f"- {attack["name"].upper()}: attack {attack["ap"]} / can use {attack["pp"]} times")

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
line()
print(f"Beginning battle between {user_character["name"]} and {opponent_character["name"]}!")
space()
turns = 0

user_character_out_of_pp = False
opponent_character_out_of_pp = False

while user_character["hp"] > 0 and opponent_character["hp"] > 0:
    if not check_if_still_have_pp(user_character["attacks"]):
        user_character_out_of_pp = True
        break
    if not check_if_still_have_pp(opponent_character["attacks"]):
        opponent_character_out_of_pp = True
        break

    turns += 1
    print(f"This is turn number #{turns}")

    space()
    print("Current HP standing:")
    print(f"{user_character["name"]} HP : {user_character["hp"]}")
    print(f"{opponent_character["name"]} HP : {opponent_character["hp"]}")
    space_line()
    print("Which attack do you want to use?")
    for index, attack in enumerate(user_character["attacks"]):
        print(f"{index+1}. {attack["name"].upper()}")
        print(f"- Attack power: {attack["ap"]}")
        print(f"- Remaining usage: {attack["pp"]}")
        print(f"- Accuracy: {attack["accuracy"]}")
    space()

    attack_choice = None
    while attack_choice == None:
        print("Enter the number of the attack")
        attack_selection_index = int(input(""))-1
        user_attacks = user_character["attacks"]
        attack_selection = user_attacks[attack_selection_index]
        if attack_selection["pp"] <= 0:
            print("The attack that you chose is not usable anymore.")
        else:
            attack_choice = attack_selection_index

    opponent_number_of_attacks = len(opponent_character["attacks"])
    opponent_attack_choice = None
    while opponent_attack_choice == None:
        opponent_attack_selection_index = random.randint(0, opponent_number_of_attacks - 1)
        opponent_attacks = opponent_character["attacks"]
        opponent_attack_selection = opponent_attacks[opponent_attack_selection_index]
        if opponent_attack_selection["pp"] > 0:
            opponent_attack_choice = opponent_attack_selection_index

    user_attack = user_character["attacks"][attack_choice]
    opponent_attack = opponent_character["attacks"][opponent_attack_choice]
    if user_character["speed"] >= opponent_character["speed"]:
        line()
        space()
        attack_turn(user_character, user_attack, opponent_character)

        if opponent_character["hp"] <= 0:
            break
        
        print(" ")

        attack_turn(opponent_character, opponent_attack, user_character)
        space()
        space_line()

        if user_character["hp"] <= 0:
            break
    else:
        line()
        attack_turn(opponent_character, opponent_attack, user_character)

        space()
        if user_character["hp"] <= 0:
            break

        attack_turn(user_character, user_attack, opponent_character)

        space_line()
        if opponent_character["hp"] <= 0:
            break



if user_character["hp"] <= 0 :
    print(f"Uh oh, {user_character["name"]} got defeated... You can always try again.")
elif opponent_character["hp"] <= 0 :
    print(f"Yay, You win! You defeated {opponent_character["name"]}!")

if user_character_out_of_pp:
    print(f"Oh no, all of {user_character["name"]}'s attacks aren't usable... You can always try again.")
if opponent_character_out_of_pp:
    print(f"Yay, you win! {opponent_character["name"]} ran out of attacks!")


# TODO:
# add poison and sleep effects