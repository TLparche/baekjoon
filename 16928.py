import sys
from collections import deque


def bfs(road, n, m):
    a1 = [0, 0, 1, -1]
    a2 = [1, -1, 0, 0]
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0, 1)])
    while queue:
        x, y, wall, depth = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return depth
        for i in range(4):
            x1, y1 = x + a1[i], y + a2[i]
            if 0 <= x1 < n and 0 <= y1 < m:
                if road[x1][y1] == '0' and not visited[x1][y1][wall]:
                    visited[x1][y1][wall] = True
                    queue.extend([(x1, y1, wall, depth + 1)])
                elif road[x1][y1] == '1' and wall == 0 and not visited[x1][y1][1]:
                    visited[x1][y1][1] = True
                    queue.extend([(x1, y1, 1, depth + 1)])
    return -1


n, m = map(int, sys.stdin.readline().strip().split())
roadmap = [list(sys.stdin.readline().strip()) for _ in range(n)]
result = bfs(roadmap, n, m)
print(result)
