import sys


def length_cal(base):
    global n
    result = 0
    for i in range(1, n + 1):
        temp_num = base // i
        if temp_num > n:
            temp_num = n
        result += temp_num
    return result


def binary_search(left, right):
    if left > right:
        print(left)
        return
    cent = (left + right) // 2
    result = length_cal(cent)
    if result >= k:
        return binary_search(left, cent - 1)
    else:
        return binary_search(cent + 1, right)


n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
binary_search(1, n * n)
