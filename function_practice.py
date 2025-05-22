# def minion_random5(integer, string1, string2):
#     if integer > 5:
#         return string1
#     else:
#         return string2

# def make_a_list(string1, string2, string3):
#     strings = []
#     strings.append(string1)
#     strings.append(string2)
#     strings.append(string3)
#     return strings

# blabla = minion_random5(7, "Happy", "Sad")

# uyxw = make_a_list("apple", "banana", "cherry")

# print(uyxw)

# def combine_list(my_list):
#     answer = ""
#     for char in my_list:
#         answer = answer + char
#     return answer
    
# result = combine_list(["D", "O", "G"])
# print(result

# def change_air_con_setting(temperature):
#     if temperature >= 35:
#         return "SUPER COOL"
#     elif temperature < 35 and temperature >= 30:
#         return "MEDIUM COOL"
#     elif temperature < 30 and temperature >= 22:
#         return "REGULAR"
#     else:
#         return "OFF"

# setting = change_air_con_setting(33.2)

# print(setting)

# def minus_supply(supplies, item, deduction):
#     if item not in supplies:
#         supplies[item] = 0

#     supplies[item] -= deduction

#     return supplies

# mini_supplies = {
#     "fartgun": 2
# }

# mini_supplies = minus_supply(mini_supplies, "fartgun", 10)

# print(mini_supplies)


import random

number = random.randint(2,100)

print(number)

list_of_things = ["George", "Enoch", "Minion"]

choice = random.choice(list_of_things)

print(choice)