import sys

input = sys.stdin.readline

n = int(input())
y_set = set()
squares = []

for _ in range(n):
    x1, x2, y1, y2 = map(int, input().split())
    y_set.add(y2)
    y_set.add(y1)
    squares.append((x1, y1, y2, 1))
    squares.append((x2, y1, y2, -1))

y_set = sorted(y_set)
len_y = len(y_set)
height = [0] * (2 * len_y)
y_index = {}
for i, v in enumerate(y_set):
    y_index[v] = i
    if i != 0:
        height[i + len_y] = (v - y_set[i - 1])

for i in range(len_y - 1, 0, -1):
    height[i] = height[2 * i] + height[2 * i + 1]
squares.sort(key=lambda x: x[0])
tree = [[0, 0] for _ in range(2 * len_y)]

prev = squares[0][0]
area = 0

for square in squares:
    x, y1, y2, loca = square
    area += tree[1][0] * (x - prev)
    prev = x

    left = y_index[y1] + len_y + 1
    right = y_index[y2] + len_y + 1
    wait = []

    while left < right:
        if left % 2:
            tree[left][0] = height[left]
            tree[left][1] += loca
            wait.append(left)
            if not tree[left][1]:
                if left < len_y:
                    tree[left][0] = tree[left * 2][0] + tree[left * 2 + 1][0]
                tree[left][0] = 0
            left += 1

        if right % 2:
            right -= 1
            wait.append(right)
            tree[right][0] = height[right]
            tree[right][1] += loca
            if not tree[right][1]:
                if right < len_y:
                    tree[right][0] = tree[right * 2][0] + tree[right * 2 + 1][0]
                else:
                    tree[right][0] = 0
        left //= 2
        right //= 2

    for i in wait:
        while i:
            if i > len_y:
                i //= 2
            if tree[i][1]:
                i //= 2
                continue
            tree[i][0] = tree[i * 2][0] + tree[i * 2 + 1][0]
            i //= 2

print(area)
