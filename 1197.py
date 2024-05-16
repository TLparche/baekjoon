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


v, e = map(int, input().split())
line = []
root_node = [i for i in range(v + 1)]
result = 0

for i in range(e):
    line.append(list(map(int, input().split())))
line.sort(key=lambda x: x[2])

for cur in line:
    if find(cur[0], root_node) != find(cur[1], root_node):
        union(cur[0], cur[1], root_node)
        result += cur[2]
print(result)