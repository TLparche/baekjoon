import sys
from collections import deque


def bfs(node, graph):
    queue = deque([(node, 0)])
    visited = set()
    res = [0, 0]
    while queue:
        vertex, distance = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbour, distance_road in graph[vertex]:
                if neighbour not in visited:
                    temp = distance + distance_road
                    queue.append((neighbour, temp))
                    if res[1] < temp:
                        res[0] = neighbour
                        res[1] = temp
    return res


v = int(sys.stdin.readline().strip())
tree = [[] for _ in range(v + 1)]
for _ in range(v):
    node_line = list(map(int, sys.stdin.readline().strip().split()))
    node = node_line[0]
    for i in range(1, len(node_line), 2):
        if node_line[i] != -1:
            tree[node].append((node_line[i], node_line[i + 1]))

first, _ = bfs(1, tree)
print(bfs(first, tree)[1])
