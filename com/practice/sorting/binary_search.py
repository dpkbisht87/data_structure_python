def binary_search_recursive(arr, min, max, key):
    if min > max:
        return
    mid = (min + max) / 2
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        max = mid - 1
    else:
        min = mid + 1
    return binary_search_recursive(arr, min, max, key)

def binary_search_iterative(arr, min, max, key):
    while min <= max:
        mid = (min + max) / 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            max = mid - 1
        else:
            min = mid + 1
    return


if __name__ =='__main__':
    arr = [23, 35, 49, 71, 85, 89, 93, 100, 102]
    key = 89
    min = 0
    max = len(arr) - 1
    print(binary_search_recursive(arr, min, max, key))
    print(binary_search_iterative(arr, min, max, key))