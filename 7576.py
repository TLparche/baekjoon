import sys
from collections import deque

a1 = [-1, 0, 0, 1]
a2 = [0, 1, -1, 0]

m, n = map(int, sys.stdin.readline().strip().split())
box = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = set()
queue = deque([])
result = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.extend([(j, i, -1)])
        elif box[i][j] == -1:
            visited.add((j, i))
while queue:
    x, y, depth = queue.popleft()
    result = depth
    if (x, y) not in visited:
        visited.add((x, y))
        for k in range(4):
            x1, y1 = x + a1[k], y + a2[k]
            if 0 <= x1 < m and 0 <= y1 < n:
                queue.append((x1, y1, depth + 1))
if len(visited) != m * n:
    print(-1)
else:
    print(result)
