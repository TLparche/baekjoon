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


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    root_node = [i for i in range(m)]
    result = 0
    road = []
    total = 0

    for i in range(n):
        x, y, z = map(int, input().split())
        road.append([x, y, z])
        total += z

    road.sort(key=lambda x: x[2])

    for cur in road:
        if find(cur[0], root_node) != find(cur[1], root_node):
            union(cur[0], cur[1], root_node)
            result += cur[2]
    print(total - result)
