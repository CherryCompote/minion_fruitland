from battle_utils import poison_type, sleep_type

sleep_effect = {
    "type": sleep_type,
    "hit_probability": 85,
    "wake_up_probability": 40
}

poison_effect = {
    "type": poison_type,
    "hit_probability": 80,
    "damage_upper": 5,
    "damage_lower": 1
}

test_character =  {
    "name": "George",
    "full_name": "George Lo",
    "speed": 80,
    "hp": 110, #Health points
    "attacks": [
        {
            "name": "test attack",
            "ap": 10, #Attack power
            "pp": 10, #How many times the player can use it
            "accuracy": 90 #how likely it is to hit the enemy
        }
    ]
}