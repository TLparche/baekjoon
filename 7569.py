import sys
from collections import deque

a1 = [-1, 0, 0, 1, 0, 0]
a2 = [0, 1, -1, 0, 0, 0]
a3 = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, sys.stdin.readline().strip().split())
box = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] for _ in range(h)]
visited = set()
queue = deque([])
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.extend([(k, j, i, -1)])
            elif box[i][j][k] == -1:
                visited.add((k, j, i))
while queue:
    x, y, z, depth = queue.popleft()
    result = depth
    if (x, y, z) not in visited:
        visited.add((x, y, z))
        for k in range(6):
            x1, y1, z1 = x + a1[k], y + a2[k], z + a3[k]
            if 0 <= x1 < m and 0 <= y1 < n and 0 <= z1 < h:
                queue.append((x1, y1, z1, depth + 1))
if len(visited) != m * n * h:
    print(-1)
else:
    print(result)
