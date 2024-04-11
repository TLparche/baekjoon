import sys


def dfs(depth, result):
    global max_num, min_num, number, operations
    if len(number) == 0:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    temp = number.pop(0)
    temp2 = result
    if operations[0] != 0:
        result += temp
        operations[0] -= 1
        dfs(depth + 1, result)
        operations[0] += 1
        result = temp2
    if operations[1] != 0:
        result -= temp
        operations[1] -= 1
        dfs(depth + 1, result)
        operations[1] += 1
        result = temp2
    if operations[2] != 0:
        result *= temp
        operations[2] -= 1
        dfs(depth + 1, result)
        operations[2] += 1
        result = temp2
    if operations[3] != 0:
        if result < 0:
            result = -result
            result //= temp
            result = -result
        else:
            result //= temp
        operations[3] -= 1
        dfs(depth + 1, result)
        operations[3] += 1
        result = temp2
    number.insert(0, temp)
    return


len_num = int(sys.stdin.readline().strip())
number = list(map(int, sys.stdin.readline().strip().split()))
operations = list(map(int, sys.stdin.readline().strip().split()))
max_num = float("-inf")
min_num = float("inf")
first_num = number[0]
number.pop(0)
dfs(1, first_num)
print(max_num)
print(min_num)
