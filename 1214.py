import sys

input = sys.stdin.readline

d, p, q = map(int, input().split())
big = max(p, q)
small = min(p, q)

left = d // big + 1
right = 0
gap = d - big * left
result = [left, right]
while left != 0:
    left -= 1
    while d - big * left - small * right > 0:
        right += 1
    if d - big * left - small * right > gap:
        gap = d - big * left - small * right
        result = [left, right]
    if gap == 0:
        break
print(result[0] * big + result[1] * small)
