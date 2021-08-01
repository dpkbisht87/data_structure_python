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
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))