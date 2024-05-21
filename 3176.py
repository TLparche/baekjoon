import math
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
range_log = int(math.log2(n)) + 1
dp = [[[0, 0, 0] for _ in range(range_log)] for _ in range(n + 1)]
nodes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

parent = [[0, 0]] * (n + 1)
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
    dp[i][0] = [parent[i][0], parent[i][1], parent[i][1]]

for i in range(1, range_log):
    for j in range(1, n + 1):
        if dp[j][i - 1][0] != 0:
            dp[j][i][0] = dp[dp[j][i - 1][0]][i - 1][0]
            dp[j][i][1] = min(dp[j][i - 1][1], dp[dp[j][i - 1][0]][i - 1][1])
            dp[j][i][2] = max(dp[j][i - 1][2], dp[dp[j][i - 1][0]][i - 1][2])

m = int(input())
for _ in range(m):
    node_a, node_b = map(int, input().split())
    if depth[node_a] > depth[node_b]:
        node_a, node_b = node_b, node_a
    min_len = float("inf")
    max_len = float("-inf")
    diff = depth[node_b] - depth[node_a]
    for i in range(range_log):
        if diff & (1 << i):
            min_len = min(min_len, dp[node_b][i][1])
            max_len = max(max_len, dp[node_b][i][2])
            node_b = dp[node_b][i][0]

    if node_a != node_b:
        for i in range(range_log - 1, -1, -1):
            if dp[node_a][i][0] != dp[node_b][i][0]:
                min_len = min(min_len, dp[node_a][i][1], dp[node_b][i][1])
                max_len = max(max_len, dp[node_a][i][2], dp[node_b][i][2])
                node_a = dp[node_a][i][0]
                node_b = dp[node_b][i][0]

        min_len = min(min_len, dp[node_a][0][1], dp[node_b][0][1])
        max_len = max(max_len, dp[node_a][0][2], dp[node_b][0][2])

    print(min_len, max_len)
