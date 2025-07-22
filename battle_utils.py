poison_type = "POISON"
sleep_type = "SLEEP"

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
