import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def find(node, root_node):
    if node != root_node[node]:
        root_node[node] = find(root_node[node], root_node)
    return root_node[node]


def union(root, child, root_node):
    root_node[child] = root


n, m = map(int, input().split())
root_node = [i for i in range(n)]
cycle_turn = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if find(a, root_node) == find(b, root_node):
        cycle_turn = i
        break
    union(find(a, root_node), find(b, root_node), root_node)

print(cycle_turn)
