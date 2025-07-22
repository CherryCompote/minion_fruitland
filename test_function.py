from test_objects import test_character, sleep_effect, poison_effect
from battle_utils import check_if_character_can_wake_up

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

new_test_character = test_character

print(new_test_character)

apply_effect(new_test_character, sleep_effect)

print(new_test_character)

apply_effect(new_test_character, poison_effect)

print(new_test_character)


apply_effect(new_test_character, sleep_effect)

print(new_test_character)


apply_effect(new_test_character, sleep_effect)

print(new_test_character)


apply_effect(new_test_character, sleep_effect)

print(new_test_character)