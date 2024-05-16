import sys

input = sys.stdin.readline

n = int(input())
dot = []
for _ in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))
dot.append(dot[0])

l, r = 0, 0
for i in range(n):
    l += dot[i][0] * dot[i + 1][1]
    r += dot[i][1] * dot[i + 1][0]

print(round(abs((l - r) / 2), 1))
