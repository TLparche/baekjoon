import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nodes = [0 for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        nodes[b] = a
    node_a, node_b = map(int, input().split())

    a_parents = [node_a]
    b_parents = [node_b]
    while nodes[node_a]:
        a_parents.append(nodes[node_a])
        node_a = nodes[node_a]

    while nodes[node_b]:
        b_parents.append(nodes[node_b])
        node_b = nodes[node_b]

    depth_a = len(a_parents) - 1
    depth_b = len(b_parents) - 1

    while a_parents[depth_a] == b_parents[depth_b]:
        depth_a -= 1
        depth_b -= 1
    print(a_parents[depth_a + 1])
