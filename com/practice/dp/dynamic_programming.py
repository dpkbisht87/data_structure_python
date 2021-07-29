from abc import abstractmethod


def longest_increasing_subseq(arr):
    if arr is None:
        return
    lis = [1] * (len(arr))
    maxLength = 1
    sum = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and 1 + lis[j] > lis[i]:
                lis[i] = lis[j] + 1
                temp = maxLength
                maxLength = max(lis[i], maxLength)
    print(lis)
    print(maxLength)

def max_increasing_subseq(a):
    # copy() available in python 3.3
    mis = a.copy()
    print(mis)
    result = 1
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j] and mis[j] + a[i] > mis[i]:
                mis[i] = mis[j] + a[i]
                result = max(mis[i], result)
    print(result)
    print(a)

def longest_common_subseq(s1, s2, m, n, arr):
    if m == - 1 or n == -1:
        return 0
    if arr[m][n] == None:
        if s1[m] == s2[n]:
            print('Common', s1[m], s2[n])
            arr[m][n] = 1 + longest_common_subseq(s1, s2, m - 1, n - 1, arr)
        else:
            arr[m][n] = max(longest_common_subseq(s1, s2, m - 1, n, arr), longest_common_subseq(s1, s2, m, n - 1, arr))
    print(arr)
    return arr[m][n]

def longest_common_substring(s1, s2, l1, l2, arr, length):
    if l1 == -1 or l2 == -1:
        return 0
    if arr[l1][l2] is None:
        if s1[l1] == s2[l2]:
            arr[l1][l2] = 1 + longest_common_substring(s1, s2, l1 -1, l2 - 1, length + 1)
        else:
            arr[l1][l2] = max(longest_common_substring(s1, s2, l1 -1, l2 - 1, arr, 0), longest_common_substring(s1, s2, l1 -1, l2 - 1, arr, 0))
    return arr[l1][l2]


def fib_tabulation_bottom_up(num):
    if num == 0 or num == 1:
        return num
    # table = [None] * (num + 1)
    # table[0] = 0
    # table[1] = 1
    # for i in range(2, num + 1):
    #     if table[i] == None:
    #         table[i]  = table[i - 1] + table[i - 2]
    # return table[num]

    first = 0
    second = 1
    for i in range(2, num + 1):
        curr = first + second
        first = second
        second = curr
    return curr

def catalan(num):
    result = [0] * (num + 1)
    result[0] = 1
    result[1] = 1

    for i in range(2, num + 1):
        for j in range(i):
            result[i] = result[i] + result[j] * result[i - j -1]
    return result[num]

def countWays_(bills, amount, maximum, memo):
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    if (amount, maximum) in memo:
        return memo[(amount, maximum)]
    ways = 0
    for bill in bills:
        if bill <= maximum:
            ways += countWays_(bills, amount-bill, bill, memo)
    memo[(amount, maximum)] = ways
    return ways

def countWaysTopDown(bills, amount):
    memo = {}
    return countWays_(bills, amount, max(bills), memo)

def countWaysBottomUp(bills, amount):
    arr = [[1 for j in range(amount + 1)] for i in range(len(bills))]
    if amount <= 0:
        return 0

    for i in range(len(bills)):
        for j in range(1, amount + 1):
            includeCurrent = 0
            excludeCurrent = 0

            if j >= bills[i]:
                includeCurrent = arr[i][j - bills[i]]
            if i > 0:
                excludeCurrent = arr[i - 1][j]
        arr[i][j] = includeCurrent + excludeCurrent

    return arr[len(bills) - 1][amount]

def rodCutting(n, prices):
    pieces = [ x + 1 for x in range(len(prices))]
    if n <= 0:
        return 0
    arr =[[0 for _ in range(n + 1)] for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(1, n + 1):
            includePiece = 0
            excludePiece = 0

            if j >= pieces[i]:
                includePiece = prices[i] + arr[i][j - pieces[i]]
            if i > 0:
                excludePiece = arr[i - 1][j]

            arr[i][j] = max(includePiece, excludePiece)
    return arr[len(prices) - 1][n]

def isSubsetSumExistsBottomUp(arr, sum):
    arr_len = len(arr)
    mat  = [[False for _ in range(sum + 1)] for _ in range(len(arr))]

    for i in range(arr_len):
        mat[i][0] = True
    # print(mat)

    for i in range(arr_len):
        for j in range(1, sum + 1):
            if mat[i - 1][j]:
                mat[i][j] = True
            else:
                if j >= arr[i]:
                    mat[i][j] = mat[i - 1][j - arr[i]]

    return mat[arr_len - 1][sum]


if __name__ == '__main__':

    #Subset Sum
    arr = [1, 2, 3, 5]
    sum = 7
    print(isSubsetSumExistsBottomUp(arr, sum))

    # Coin Change Problem
    # print(countWaysTopDown([1,2,5], 5))
    # print(countWaysBottomUp([10,20], 30))

    # Rod cutting
    # n = 4
    # prices = [2, 3, 7, 8]
    # print(rodCutting(n, prices))

    # Catalan Number
    # print(catalan(6))

    # arr = [7,1, 4, 8, 11, 2, 14, 3]
    # longest_increasing_subseq(arr)
    # max_increasing_subseq(arr)

    # s1 = 'abde'
    # s2 = 'acb'
    # arr = [[None] * len(s2)]  * len(s1)
    # print(arr)
    # print(longest_common_subseq(s1, s2, len(s1) - 1, len(s2) - 1, arr))

    # s1 = 'abcde'
    # s2 = 'bcd'
    # arr = [[None] * len(s2)] * len(s1)
    # print(arr)
    # print(longest_common_substring(s1, s2, len(s1) -1, len(s2) - 1, arr, 0))


    # Fibonacci number tabulation (bottom up)
    # print(fib_tabulation_bottom_up(10000))




