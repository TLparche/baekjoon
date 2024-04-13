import sys


def multi_matrix(a, b):
    global div
    temp = [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3], a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3]]
    for i in range(4):
        temp[i] %= div
    return temp


def divide(k):
    global base_matrix
    if k == 1:
        return base_matrix
    if k % 2 == 1:
        return multi_matrix(divide(k - 1), base_matrix)
    else:
        temp = divide(k // 2)
        return multi_matrix(temp, temp)


base_matrix = [1, 1, 1, 0]
div = 1000000007
n = int(sys.stdin.readline().strip())
print(divide(n)[1])
