import sys

input = sys.stdin.readline

mod = 10 ** 9 + 7

stars = []
n = int(input())
for _ in range(n):
    stars.append(list(map(int, input().split())))
stars.sort(key=lambda x: x[1])

temp = 0
for i in range(n - 1):
    if stars[i][1] != stars[i + 1][1]:
        stars[i][1] = temp
        temp += 1
    else:
        stars[i][1] = temp

stars[n - 1][1] = temp
stars.sort(key=lambda x: (x[0], -x[1]))

tree = [[0, 0] for _ in range(2 * n)]
result = 0
before = 10 ** 6
count = 0
stack = []
for i in stars:
    x, y = i

    if before != x and stack:
        for j in stack:
            before_y, before_left_top = j
            while before_y:
                tree[before_y][0] += 1
                tree[before_y][1] += before_left_top
                if before_y % 2:
                    before_y -= 1
                before_y //= 2
        stack = []

    left_top = 0
    left_down = 0
    left = y + n + 1
    right = 2 * n - 1
    while left < right:
        if left % 2:
            left_top += tree[left][0] % mod
            left += 1
        if right % 2:
            right -= 1
            left_top += tree[right][0] % mod
        left //= 2
        right //= 2

    left = n
    right = y + n
    while left < right:
        if left % 2:
            left_down += tree[left][1] % mod
            left += 1
        if right % 2:
            right -= 1
            left_down += tree[right][1] % mod
        left //= 2
        right //= 2
    result += left_down % mod

    left_top %= mod
    left_down %= mod
    stack.append([y + n, left_top])
    before = x

print(result % mod)
