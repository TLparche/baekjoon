import sys


def floyd_warshall(dist, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
    return dist[1:]


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
dist = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    dist[a][b] = min(dist[a][b], c)
for i in range(1, n + 1):
    dist[i][i] = 0
res = floyd_warshall(dist, n)
for i in res:
    for j in i[1:]:
        if j == float("inf"):
            print(0, end=" ")
        else:
            print(j, end=" ")
    sys.stdout.write("\n")
