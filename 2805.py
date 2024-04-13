import sys


def length_cal(height):
    global line
    result = 0
    for i in line:
        temp_result = i - height
        if temp_result > 0:
            result += temp_result
    return result


def binary_search(value):
    global temp
    gap = abs(value - temp[-1])
    jump = gap // 2
    if gap // 2 != gap / 2:
        jump += 1
    temp.append(value)
    if gap == 1:
        return
    if value == 0:
        return binary_search(value + jump)
    result = length_cal(value)
    if result >= n:
        return binary_search(value + jump)
    else:
        return binary_search(value - jump)


k, n = map(int, sys.stdin.readline().strip().split())
line = list(map(int, sys.stdin.readline().strip().split()))
temp = [0]
binary_search(max(line))
temp.sort(reverse=True)
for i in temp:
    height = length_cal(i)
    if height == n:
        print(i)
        break
    if height > n:
        print(i)
        break
