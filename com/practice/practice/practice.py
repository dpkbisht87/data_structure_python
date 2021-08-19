
def first_non_repeating_character(s):
    temp = dict()
    for item in s:
        if item in temp.keys():
            temp[item] = temp[item] + 1
        else:
            temp[item] = 1

    print(temp)
    for i in s:
        if temp[i] == 1:
            return i


s1 = 'aaaaa'

# print(first_non_repeating_character(s1))


def rotate90Clockwise(a, N):
    result =[[0 for _ in range(N)] for _ in range(N)]
    for i in reversed(range(N)):
        for j in range(N):
            result[j][N - i - 1] = a[i][j]
    return result

a = [[0  for i in range(3) ] for j in range(3)]
count = 1
for i in range(3):
    for j in range(3):
        a[i][j] = count
        count += 1
# a = rotate90Clockwise(a, 3)
# for i in range(3):
#     print(a[i][0], a[i][1], a[i][2], end = '')
#     print()



def firstDuplicate(n):
    check =[False] * (len(n) + 1)
    print(check)
    for i in n:
        if check[i]:
            return i
        check[i] = True
    return -1

def firstDuplicateWithoutSpace(a):
    for i in range(len(a)):
        if a[a[i]-1]  < 0:
            return i
        a[a[i] - 1] = (a[a[i] - 1]) * -1
        print(a)
    return -1


n = [2,1,3,5,3,2]
# print(firstDuplicate(n))
# print(firstDuplicateWithoutSpace(n))

def increment_as_string(n):
    return 1 + int(n)



n = '999'
# print(increment_as_string(n))
# print(increment_as_string_impl(n))

def read_file(file_path):
    with open(file_path, 'a') as f:
        f.write('HelloWorld')

read_file('/Users/dbisht/test.sh')

# result = []
# day = 1
# for date in range(checkin, checkout):
#     rooms = available_rooms[date]
#     for room in rooms:
#         if room.availability > 0:
#             if room.features == 'breakfast':
#                 for selected_room in result:
#                     room.price = selected_room.price + room.price
#                     room.feature = intersection(selected_room.features, room.features)
#                 result.append(option_room)




def modify_dict(tmp=None):
    tmp[2] = 'oi'

dict1 = {1:'hello', 2 :' hi', 3:'bye'}
print(dict1)
modify_dict(dict1.copy())
print(dict1)