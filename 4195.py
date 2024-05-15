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


input = sys.stdin.readline

for _ in range(int(input().strip())):
    f = int(input().strip())
    root_node = {}
    size = {}
    dict = {}

    for _ in range(f):
        id1, id2 = input().split()
        if id1 not in dict:
            dict[id1] = len(dict)
            root_node[dict[id1]] = dict[id1]
            size[dict[id1]] = 1
        if id2 not in dict:
            dict[id2] = len(dict)
            root_node[dict[id2]] = dict[id2]
            size[dict[id2]] = 1
        union(dict[id1], dict[id2], root_node, size)
        first_friend = dict[id1]
        friends = size[find(first_friend, root_node)]
        print(friends)
