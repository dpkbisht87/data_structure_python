# BINARY SEARCH - 1.Iterative 2.Recursive
################################################################################################################################################################
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binary_search_recursive(data, target, low, high):
    mid = (low + high) // 2
    if data[mid] == target:
        return True
    elif data[mid] > target:
        return binary_search_recursive(data, target, low, mid - 1)
    else:
        return binary_search_recursive(data, target, mid + 1, high)

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37

# print(binary_search_recursive(data, target, 0, len(data)-1))
# print(binary_search_iterative(data, target))

# FIND CLOSEST NUMBER
################################################################################################################################################################

def find_closest_num(A, target):
    min_diff = min_diff_left = min_diff_right = float('inf')
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == A[mid]:
            return A[mid]
        else:
            if target < A[mid]:
                if target > A[mid - 1]:
                    if target - A[mid - 1] < A[mid] - target:
                        return A[mid - 1]
                    else:
                        return A[mid]
                else:
                    high = mid - 1
            else:
                if target < A[mid + 1]:
                    if target - A[mid] < A[mid + 1] - target:
                        return A[mid]
                    else:
                        return A[mid + 1]
                else:
                    low = mid + 1


# A1 = [1, 2, 4, 5, 6, 6, 8, 9]
# A2 = [2, 5, 6, 7, 8, 8, 9]

# print(find_closest_num(A1, 11))
# print(find_closest_num(A2, 4))

# FIND FIXED POINT SUCH THAT A[i] = i
################################################################################################################################################################

def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] == mid:
            return A[mid]
        elif A[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    return None



A1 = [-10, -5, 0, 3, 7]
A2 = [0, 2, 5, 8, 17]
A3 = [-10, -5, 3, 4, 7, 9]
# print(find_fixed_point(A3))

# FIND HIGHEST ELEMENT
################################################################################################################################################################

def find_highest_number(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid - 1] < A[mid] and A[mid + 1] < A[mid]:
            return A[mid]
        elif A[mid - 1] < A[mid] and A[mid + 1] > A[mid]:
            low = mid + 1
        else:
            high = mid - 1

A = [5, 4, 3, 2, 1]
A = [1, 6, 5, 4, 3, 2, 1]

# print(find_highest_number(A))

# FIRST ENTRY WITH DUPLICATES
################################################################################################################################################################

def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] == target:
            while A[mid] == target:
                mid -=1
            return mid + 1
        elif target < A[mid]:
            high = mid - 1
        else:
            low = mid + 1




A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
print(find(A, target))
