import sys

input = sys.stdin.readline


def update(node, wait):
    global tree, tree_num, lazy
    wait.append([node, d * tree_num[node]])
    tree[node] += d * tree_num[node]
    if tree_num[node] != 1:
        lazy[2 * node] += d * tree_num[2 * node]
        lazy[2 * node + 1] += d * tree_num[2 * node + 1]
    return wait


def calculate(node, wait):
    global tree, tree_num, lazy
    wait.append(node)
    temp_node = node
    temp_li = []
    while temp_node:
        temp_li.append(temp_node)
        temp_node //= 2

    for i in temp_li[::-1]:
        if lazy[i] != 0:
            temp = tree_num[i]
            ori = lazy[i] // temp
            if temp != 1:
                lazy[2 * i] += ori * tree_num[2 * i]
                lazy[2 * i + 1] += ori * tree_num[2 * i + 1]
            tree[i] += lazy[i]
            lazy[i] = 0

    return wait


n = int(input())
tree = [0] * (2 * n)
tree_num = [0] * (2 * n)
lazy = [0] * (2 * n)

numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    tree[i + n] = numbers[i]
    tree_num[i + n] = 1

m = int(input())

for i in range(n - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]
    tree_num[i] = tree_num[2 * i] + tree_num[2 * i + 1]

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, b, c, d = query
        left = b + n - 1
        right = c + n
        wait = []

        while left < right:
            if left % 2:
                wait = update(left, wait)
                left += 1
            if right % 2:
                right -= 1
                wait = update(right, wait)
            left //= 2
            right //= 2

        for i, j in wait:
            while i:
                i //= 2
                tree[i] += j

    elif query[0] == 2:
        _, b = query
        result = 0
        left = b + n - 1
        right = b + n
        wait = []
        while left < right:
            if left % 2:
                wait = calculate(left, wait)
                left += 1

            if right % 2:
                right -= 1
                wait = calculate(right, wait)
            left //= 2
            right //= 2

        for i in wait:
            result += tree[i]
        print(result)
