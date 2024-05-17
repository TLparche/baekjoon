import math
import itertools
import sys

input = sys.stdin.readline


def is_convex(li):
    for i in range(8):
        left = (i - 1) % 8
        right = (i + 1) % 8
        if not (li[left] * li[right] * math.sqrt(2) <= li[i] * (li[left] + li[right])):
            return False
    return True


node = list(map(int, input().split()))

node_permutations = itertools.permutations(node)

result = 0
for perm in node_permutations:
    if is_convex(perm):
        result += 1

print(result)
