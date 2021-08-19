def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = "Was it a cat I saw?"
# print(is_palindrome(s))


def is_anagram(s1, s2):
    temp1 = dict()
    for i in s1:
        if i.isalnum():
            if i in temp1.keys():
                temp1[i] = temp1[i] + 1
            else:
                 temp1[i] = 1

    for j in s2:
        if j.isalnum():
            if j in temp1.keys():
                temp1[j] = temp1[j] - 1
            else:
                return False

    for value in temp1.values():
        if value > 0:
            return False
    return True

s1 = "fairy taldaes"
s2 = "adrail safety"
## normalizing the strings
# s1 = s1.replace(" ", "").lower()
# s2 = s2.replace(" ", "").lower()

# print(is_anagram(s1, s2))


def is_palin_perm(s):
    l = len(s)

    if l % 2 == 0:
        first_end = l / 2
    else:
       first_end = (l / 2) - 1

    temp = dict()
    for i in range(first_end + 1):
        cur = s[i].lower()
        if cur.isalnum():
            if cur in temp.keys():
                temp[cur] += 1
            else:
                temp[cur] = 1

    print('itr1',temp)
    print(first_end, l)
    for j in range(first_end, l + 1):
        cur =s[j].lower()
        print(cur)
        if cur.isalnum():
            if cur in temp.keys():
                temp[cur] -= 1
            else:
                return False
    print('itr2',temp)

    for value in temp.values():
        if value > 0:
            return False
    return True

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

# print(is_palin_perm(palin_perm))
# print(is_palin_perm(not_palin_perm))






def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    temp = dict()
    for i in s1:
        if i in temp.keys():
            temp[i] += 1
        else:
            temp[i] = 1

    for j in s2:
        if j in temp.keys():
            temp[j] -= 1
        else:
            return False
    return all(value == 0 for value in temp.values())

is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"

# print(is_permutation(is_permutation_1, is_permutation_2))
# print(is_permutation(not_permutation_1, not_permutation_2))


def int_to_str(input_int):
    temp = []
    while input_int != 0:
        remainder = input_int % 10
        print(chr(65+remainder))
        temp.append(chr(65+remainder))
        input_int = input_int // 10
    print(temp)
    result = ''
    for i in reversed(range(len(temp))):
        val = ord(temp[i]) - 65
        print(val)
        print(type(val))

input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))