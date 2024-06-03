from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == sink:
                    return True
    return False


def edmonds_karp(graph, source, sink):
    copy_graph = [row[:] for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(copy_graph, source, sink, parent):
        path_flow = float('Inf')
        cur = sink

        while cur != source:
            path_flow = min(path_flow, copy_graph[parent[cur]][cur])
            cur = parent[cur]

        max_flow += path_flow

        cur = sink
        while cur != source:
            cur_parent = parent[cur]
            copy_graph[cur_parent][cur] -= path_flow
            copy_graph[cur][cur_parent] += path_flow
            cur = parent[cur]
        parent = [-1] * len(graph)
    return max_flow


n, p = map(int, input().split())
way = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(p):
    a, b = map(int, input().split())
    way[a][b] = 1
print(edmonds_karp(way, 1, 2))
