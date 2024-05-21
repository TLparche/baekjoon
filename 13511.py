import math
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
range_log = int(math.log2(n)) + 1
dp = [[[0, 0] for _ in range(range_log)] for _ in range(n + 1)]
nodes = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

parent = [[0, 0] for _ in range(n + 1)]
depth = [0] * (n + 1)
visited = [0] * (n + 1)

queue = deque([1])
visited[1] = 1
while queue:
    cur = queue.popleft()
    for i, j in nodes[cur]:
        if not visited[i]:
            queue.append(i)
            depth[i] = depth[cur] + 1
            parent[i] = [cur, j]
            visited[i] = 1

for i in range(1, n + 1):
    dp[i][0] = [parent[i][0], parent[i][1]]

for i in range(1, range_log):
    for j in range(1, n + 1):
        if dp[j][i - 1][0] != 0:
            dp[j][i][0] = dp[dp[j][i - 1][0]][i - 1][0]
            dp[j][i][1] = dp[j][i - 1][1] + dp[dp[j][i - 1][0]][i - 1][1]

m = int(input())
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, node_u, node_v = query
    else:
        _, node_u, node_v, k = query
    u, v = node_u, node_v
    if depth[u] > depth[v]:
        u, v = v, u
    diff = depth[v] - depth[u]

    length = 0
    for i in range(range_log):
        if diff & (1 << i):
            length += dp[v][i][1]
            v = dp[v][i][0]
    if u == v:
        ancestor = u
    else:
        for i in range(range_log - 1, -1, -1):
            if dp[u][i][0] != dp[v][i][0]:
                length += dp[u][i][1] + dp[v][i][1]
                u = dp[u][i][0]
                v = dp[v][i][0]
        ancestor = dp[u][0][0]
        length += dp[u][0][1] + dp[v][0][1]
    if query[0] == 1:
        print(length)
    else:
        if k <= depth[node_u] - depth[ancestor]:
            k -= 1
            cur = node_u
        else:
            k = depth[node_v] + depth[node_u] - 2 * depth[ancestor] - k + 1
            cur = node_v

        for i in range(range_log):
            if k & 1 << i:
                cur = dp[cur][i][0]
        print(cur)
