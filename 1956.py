import sys


def floyd_warshall(dist, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
    return dist


n, m = map(int, sys.stdin.readline().strip().split())
dist = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    dist[a][b] = c
res = floyd_warshall(dist, n)
short = float("inf")
for i in range(1, n + 1):
    short = min(short, res[i][i])
if short == float("inf"):
    print(-1)
else:
    print(short)
