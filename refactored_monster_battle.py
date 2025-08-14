from battle_utils import intro, select_user_character, select_opponent_character, start_battle_description, check_remaining_pp, apply_poison_damage, check_remaining_hp, apply_effect, select_attack
from warriors import demo_list_of_warriors, full_list_of_warriors
from test_objects import poison_effect

list_of_characters = demo_list_of_warriors
# list_of_characters = full_list_of_warriors

# 1. Intro
intro()

# 2. User character selection
# user_character = select_user_character(list_of_characters)
user_character = list_of_characters[0]

# 3. Opponent character selection
# opponent_character = select_opponent_character(list_of_characters, user_character)
opponent_character = list_of_characters[1]

# 4. Battle description
start_battle_description(user_character, opponent_character)

# 5. Enter battle loop
user_lost = False
opponent_lost = False

while not (user_lost or opponent_lost):
    
    # 5a. Check remaining PP for both characters
    user_lost = not check_remaining_pp(user_character["attacks"])
    opponent_lost = not check_remaining_pp(opponent_character["attacks"])

    if user_lost or opponent_lost:
        break

    # 5b. Apply poison damage to both characters and check if no more hp
    apply_poison_damage(user_character)
    user_lost = not check_remaining_hp(user_character)
    if user_lost:
        break

    apply_poison_damage(opponent_character)
    opponent_lost = not check_remaining_hp(opponent_character)
    if opponent_lost:
        break

    input("Press enter for next step")







if user_lost and opponent_lost:
    print("its a draw")
elif user_lost:
    print("user lost")
elif opponent_lost:
    print("opoonent lost")