def array_advance(A):
    furthest_reached = 0
    last_index = len(A) - 1
    for i in range(len(A)):
        if i > furthest_reached:
            return False
        furthest_reached = max(furthest_reached,  A[i] + i)
    return furthest_reached >= last_index

# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
# print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
# print(array_advance(A))

##########################################
A1 = [1, 4, 9]

A2 = [9, 9, 9]

# s = ''.join(map(str, A))
# print(int(s) + 1)


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


# print(plus_one(A1))
# print(plus_one(A2))

##########################################

def two_sum(A, target):
    temp = dict()
    for item in A:
        diff = target - item
        if diff in temp.keys():
            print(diff, item)
            return True
        else:
            temp[item] = 1
    return False

def two_sum_using_pointers(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
# print(two_sum(A,target))
# print(two_sum_using_pointers(A,target))
target = 20
# print(two_sum(A,target))
# print(two_sum_using_pointers(A,target))

##########################################

def intersect_sorted_array(A, B):
    i = 0
    j = 0
    len_A = len(A)
    len_B = len(B)
    result = []
    while i < len_A and j < len_B:
        if A[i] == B[j]:
            print(result)
            if i == 0 or A[i] != A[i - 1]:
                result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return result


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_array(A, B))