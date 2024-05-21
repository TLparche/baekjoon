import math
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
range_log = int(math.log2(n)) + 1
dp = [[0 for _ in range(range_log)] for _ in range(n + 1)]
nodes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
visited = [0] * (n + 1)

queue = deque([1])
visited[1] = 1
while queue:
    cur = queue.popleft()
    for i in nodes[cur]:
        if not visited[i]:
            queue.append(i)
            depth[i] = depth[cur] + 1
            parent[i] = cur
            visited[i] = 1

for i in range(1, n + 1):
    dp[i][0] = parent[i]

for i in range(1, range_log):
    for j in range(1, n + 1):
        if dp[j][i - 1] != 0:
            dp[j][i] = dp[dp[j][i - 1]][i - 1]

m = int(input())
for _ in range(m):
    node_a, node_b = map(int, input().split())

    if depth[node_a] > depth[node_b]:
        node_a, node_b = node_b, node_a
    diff = depth[node_b] - depth[node_a]

    for i in range(range_log):
        if diff & (1 << i):
            node_b = dp[node_b][i]

    if node_a == node_b:
        print(node_a)
        continue

    for i in range(range_log - 1, -1, -1):
        if dp[node_a][i] != dp[node_b][i]:
            node_a = dp[node_a][i]
            node_b = dp[node_b][i]

    print(dp[node_a][0])
