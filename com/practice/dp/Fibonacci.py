def get_fib_iterative(n):
    if n in [0,1]:
        return n
    return get_fib_iterative(n - 1) + get_fib_iterative(n - 2)


def get_fib_top_down(n, arr):
    if n < 2:
        return n
    if arr[n] == 0:
        arr[n] = get_fib_top_down(n - 1, arr) + get_fib_top_down(n - 2, arr)  
    return arr[n]     

def get_fib_bottom_up(n):
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, len(arr)):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

if __name__ == '__main__':
    val = 10
    # print(get_fib_iterative(10))

    # Top Down approach
    arr = [0] * (val + 1)
    print(get_fib_top_down(val, arr))

    # Bottom up approach
    print(get_fib_bottom_up(val))
