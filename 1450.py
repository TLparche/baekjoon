import sys
from itertools import combinations


def subset(item_list):
    subsets = []
    for i in range(len(item_list) + 1):
        for j in combinations(item_list, i):
            subsets.append(sum(j))
    return subsets


n, c = map(int, sys.stdin.readline().strip().split())
items = list(map(int, sys.stdin.readline().strip().split()))
result = 0

a_items = items[:n // 2]
b_items = items[n // 2:]
a_subset = sorted(subset(a_items))
b_subset = subset(b_items)

for b in b_subset:
    if b > c:
        continue

    left = 0
    right = len(a_subset) - 1

    while left <= right:
        mid = (left + right) // 2
        if a_subset[mid] + b > c:
            right = mid - 1
        else:
            left = mid + 1

    result += right + 1

print(result)
