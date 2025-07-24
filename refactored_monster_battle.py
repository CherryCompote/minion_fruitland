from battle_utils import intro, select_user_character
from warriors import demo_list_of_warriors, full_list_of_warriors

list_of_characters = demo_list_of_warriors
# list_of_characters = full_list_of_warriors

# 1. Intro
intro()

# 2. User character selection
user_character = select_user_character(list_of_characters)