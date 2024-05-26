import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = []
for i in range(n):
    numbers.append(int(input()))

tree = [[0, 0] for _ in range(2 * n)]
for i in range(n):
    tree[n + i] = [numbers[i], numbers[i]]

for i in range(n - 1, 0, -1):
    for j in range(2):
        tree[i][0] = min(tree[2 * i][0], tree[2 * i + 1][0])
        tree[i][1] = max(tree[2 * i][1], tree[2 * i + 1][1])

for _ in range(m):
    a, b = map(int, input().split())

    min_num = 10 ** 10
    max_num = 0
    a += n - 1
    b += n
    while a < b:
        if a % 2:
            min_num = min(min_num, tree[a][0])
            max_num = max(max_num, tree[a][1])
            a += 1
        if b % 2:
            b -= 1
            min_num = min(min_num, tree[b][0])
            max_num = max(max_num, tree[b][1])
        a //= 2
        b //= 2
    print(min_num, max_num)
