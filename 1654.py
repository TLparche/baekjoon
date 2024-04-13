import sys


def binary_search(value):
    global line, temp
    gap = abs(value - temp[-1])
    jump = gap // 2
    if gap // 2 != gap / 2:
        jump += 1
    temp.append(value)
    if gap == 1:
        return
    if value == 0:
        return binary_search(value + jump)
    result = 0
    for i in line:
        result += i // value

    if result >= n:
        return binary_search(value + jump)
    else:
        return binary_search(value - jump)


k, n = map(int, sys.stdin.readline().strip().split())
line = []
for i in range(k):
    line.append(int(sys.stdin.readline().strip()))
temp = [0]
binary_search(max(line))
temp.sort(reverse=True)
print(temp)
for i in temp:
    cut = 0
    for j in line:
        cut += j // i
    if cut >= n:
        print(i)
        break
