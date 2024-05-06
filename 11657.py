import sys


def bellman_ford(graph, start, n):
    dist = [float("Inf")] * (n + 1)
    dist[start] = 0

    for _ in range(n):
        for i in range(1, n + 1):
            if i in graph:
                for v, w in graph[i]:
                    if dist[i] != float("Inf") and dist[i] + w < dist[v]:
                        dist[v] = dist[i] + w

    for i in range(1, n + 1):
        if i in graph:
            for v, w in graph[i]:
                if dist[i] != float("Inf") and dist[i] + w < dist[v]:
                    return [-1]

    return dist[2:]


graph = {}

n, m = map(int, sys.stdin.readline().strip().split())
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a in graph:
        graph[a].append((b, c))
    else:
        graph[a] = [(b, c)]

if 1 not in graph:
    for _ in range(n-1):
        print(-1)
else:
    res = bellman_ford(graph, 1, n)
    for i in res:
        if i == float("Inf"):
            print(-1)
        else:
            print(i)
