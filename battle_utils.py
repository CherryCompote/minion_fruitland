
from monster_battle_types import sleep_type, poison_type
from formatting import space, line, space_line

def intro():
    print("Welcome to monster battle! In this game, you try to defeat other warriors!")

def select_user_character(list_of_warriors):

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
        space()
        confirm_character_answer = input("Do you want to use this character or not? (yes/no)")

        if confirm_character_answer == "yes":
            selected_character = True
            user_character = character_details

    return user_character


def check_if_still_have_pp(attack_list):
    for attack in attack_list:
        if attack["pp"] > 0:
            return True
    return False

# attacker is a dict
# attack is a dict
# defender is a dict
def attack_turn(attacker, attack, defender):
    attack_chance = random.randint(1, 100)
    if attack_chance <= attack["accuracy"]:
        print(f"{attacker["full_name"]} used {attack["name"].upper()}!")
        print(f"{defender["full_name"]} lost {attack["ap"]} HP")
        defender["hp"] -= attack["ap"]
    else:
        print(f"{attacker["full_name"]} used {attack["name"].upper()} but missed!")
        print(f"{defender["full_name"]} was unharmed.")
    attack["pp"] -= 1
        
def check_if_character_can_wake_up(character):
    if character["sleep_effect"]:
        wake_up_probability = character["sleep_effect"]["wake_up_probability"]
        wake_up_chance = random.randint(1, 100)
        if wake_up_chance <= wake_up_probability:
            return True
        else:
            return False
    return True

#checks if character is effected by any effects, if so, check if the effect applied is same asthe one we are applying,
#if so, break, if not, apply the effect. if character isn't effected by any effects, add effected and apply the effect.
def apply_effect(character, effect):
    if "effected" in character:
        effect_type = effect["type"]
        already_has_same_effect = False
        for effected_effect in character["effected"]:
            if effect_type == effected_effect["type"]:
                already_has_same_effect = True

        if not already_has_same_effect:
            character["effected"].append(effect)
    else:
        # if charactyer has no effects, then we can definitely apply the effect
        character["effected"] = [effect]

