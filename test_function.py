from warriors import demo_list_of_warriors
from test_objects import test_character, sleep_effect, poison_effect
from battle_utils import check_if_character_can_wake_up
from formatting import space, line, space_line

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



a = select_user_character(demo_list_of_warriors)
print(a) 