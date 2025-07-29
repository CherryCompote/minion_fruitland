from battle_utils import intro, select_user_character, select_opponent_character, start_battle_description, check_remaining_pp
from warriors import demo_list_of_warriors, full_list_of_warriors

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
gameover = False
user_lost = False
opponent_lost = False
while not gameover:
    
    # 5a. Check remaining PP for both characters
    user_lost = not check_remaining_pp(user_character["attacks"])
    opponent_lost = not check_remaining_pp(opponent_character["attacks"])

    if user_lost or opponent_lost:
        break
