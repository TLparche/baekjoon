import sys

sys.setrecursionlimit(10 ** 9)


def find(node):
    global root_node
    if node != root_node[node]:
        root_node[node] = find(root_node[node])
    return root_node[node]


def adjoint(root, child):
    global root_node
    l_root = find(root)
    r_root = find(child)
    if l_root != r_root:
        root_node[r_root] = l_root
    return


n, m = map(int, sys.stdin.readline().strip().split())
root_node = [i for i in range(n + 1)]
for _ in range(m):
    order = list(map(int, sys.stdin.readline().strip().split()))
    if order[0] == 0:
        adjoint(order[1], order[2])
    elif order[0] == 1:
        if find(order[1]) == find(order[2]):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
