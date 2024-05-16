import sys

input = sys.stdin.readline


def find(node, root_node):
    if node != root_node[node]:
        root_node[node] = find(root_node[node], root_node)
    return root_node[node]


def union(root, child, root_node):
    l_root = find(root, root_node)
    r_root = find(child, root_node)
    if l_root != r_root:
        root_node[r_root] = l_root


def distance(a, b):
    x = abs(a[1] - b[1])
    y = abs(a[2] - b[2])
    return (x ** 2 + y ** 2) ** 0.5


n, m = map(int, input().split())
line = []
root_node = [i for i in range(n + 1)]
result = 0
star = []
complete = []

for i in range(n):
    x, y = map(int, input().split())
    star.append([i+1, x, y])
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y, root_node)

for i in range(n - 1):
    for j in range(i + 1, n):
        line.append([star[i][0], star[j][0], distance(star[i], star[j])])
line.sort(key=lambda x: x[2])

for cur in line:
    if find(cur[0], root_node) != find(cur[1], root_node):
        union(cur[0], cur[1], root_node)
        result += cur[2]
print(format(result, ".2f"))
