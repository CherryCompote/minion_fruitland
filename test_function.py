import random
from warriors import demo_list_of_warriors
from test_objects import test_character, sleep_effect, poison_effect
from battle_utils import check_if_character_can_wake_up, select_opponent_character, select_user_character, apply_effect
from formatting import space, line, space_line
from monster_battle_types import poison_type, sleep_type

a = select_opponent_character(demo_list_of_warriors, demo_list_of_warriors[0])
