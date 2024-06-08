from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(u, adj, pair_v, visited):
    for v in adj[u]:
        if not visited[v - n]:
            visited[v - n] = True
            if pair_v[v] == 0 or dfs(pair_v[v], adj, pair_v, visited):
                pair_v[v] = u
                return True
    return False


def maximum_matching(U, V, adj):
    pair_v = {}
    for v in V:
        pair_v[v] = 0

    match_count = 0
    for u in U:
        visited = [False] * (m + 1)
        if dfs(u, adj, pair_v, visited):
            match_count += 1
        visited = [False] * (m + 1)
        if dfs(u, adj, pair_v, visited):
            match_count += 1
        if match_count == m:
            return m
    return match_count


n, m = map(int, input().split())
adj = defaultdict(list)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    k = data[0]
    for j in range(1, k + 1):
        adj[i].append(data[j] + n)

U = list(range(1, n + 1))
V = list(range(n + 1, n + m + 1))

print(maximum_matching(U, V, adj))
