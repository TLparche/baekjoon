import sys


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


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
root_node = [i for i in range(n+1)]
for i in range(n):
    connect = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(n):
        if connect[j] == 1:
            adjoint(i + 1, j + 1)

plan = list(map(int, sys.stdin.readline().strip().split()))
plan_set = set(plan)

base = find(plan[0])
for i in plan_set:
    if find(i) != base:
        print("NO")
        break
else:
    print("YES")
