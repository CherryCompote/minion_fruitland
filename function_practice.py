def minion_random5(integer, string1, string2):
    if integer > 5:
        return string1
    else:
        return string2

def make_a_list(string1, string2, string3):
    strings = []
    strings.append(string1)
    strings.append(string2)
    strings.append(string3)
    return strings

blabla = minion_random5(7, "Happy", "Sad")

uyxw = make_a_list("apple", "banana", "cherry")

print(uyxw)

def combine_list(my_list):
    answer = ""
    for char in my_list:
        answer = answer + char
    return answer
    
result = combine_list(["D", "O", "G"])
print(result)
    