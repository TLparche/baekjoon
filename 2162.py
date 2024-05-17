import sys


def find(node, root_node):
    if node != root_node[node]:
        root_node[node] = find(root_node[node], root_node)
    return root_node[node]


def union(root, child, root_node, size):
    l_root = find(root, root_node)
    r_root = find(child, root_node)
    if l_root != r_root:
        root_node[r_root] = l_root
        size[l_root] += size[r_root]
        del size[r_root]


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


def is_cross(first, second):
    x1, y1, x2, y2 = first
    x3, y3, x4, y4 = second
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3,
                                                                                                            y4) <= max(
            y1, y2):
            return 1
    else:
        if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
            return 1
    return 0


input = sys.stdin.readline

lines = []
size = {}
n = int(input())
root_node = [i for i in range(n + 1)]
for i in range(n):
    lines.append(list(map(int, input().split())))
    size[i] = 1

for i in range(n - 1):
    for j in range(i + 1, n):
        if is_cross(lines[i], lines[j]):
            if root_node[i] != root_node[j]:
                union(i, j, root_node, size)

print(len(size))
result = 0
for i in size:
    if result < size[i]:
        result = size[i]
print(result)
