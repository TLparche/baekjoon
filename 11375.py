from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def bfs(U, pair_u, pair_v, dist):
    queue = deque()
    for u in U:
        if pair_u[u] == 0:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    dist[0] = float('inf')
    while queue:
        u = queue.popleft()
        if dist[u] < dist[0]:
            for v in adj[u]:
                if dist[pair_v[v]] == float('inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[0] != float('inf')


def dfs(u, adj, dist):
    if u != 0:
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u] + 1:
                if dfs(pair_v[v], adj, dist):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = float('inf')
        return False
    return True


def hopcroft_karp(U, V, adj):
    for u in U:
        pair_u[u] = 0
    for v in V:
        pair_v[v] = 0
    matching = 0

    while bfs(U, pair_u, pair_v, dist):
        for u in U:
            if pair_u[u] == 0:
                if dfs(u, adj, dist):
                    matching += 1
    return matching


n, m = map(int, input().split())
adj = defaultdict(list)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    k = data[0]
    for j in range(1, k + 1):
        adj[i].append(data[j] + n)

pair_u = {}
pair_v = {}
dist = {}
U = list(range(1, n + 1))
V = list(range(n + 1, n + m + 1))

print(hopcroft_karp(U, V, adj))
