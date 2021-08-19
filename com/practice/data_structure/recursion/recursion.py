def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]

def find_uppercase_recursive(input_str):
    if len(input_str) == 0:
        return
    if input_str[:1].isupper():
        return input_str[:1]
    else:
        return find_uppercase_recursive(input_str[1:])



input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"


# print(find_uppercase_iterative(input_str_1))
# print(find_uppercase_iterative(input_str_2))
# print(find_uppercase_iterative(input_str_3))

# print(find_uppercase_recursive(input_str_1))
# print(find_uppercase_recursive(input_str_2))
# print(find_uppercase_recursive(input_str_3))

vowels = "aeiou"

def recursive_count_consonants(input_str):
    if input_str == '':
        return 0
    if input_str[:1].lower() not in vowels:
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])



print(recursive_count_consonants('LuCiDPrograMMiNG'))