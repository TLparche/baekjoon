import sys
from collections import deque

a1 = [-1, 1]
a2 = [-2, 2]


def bfs(start_x, start_y, des_x, des_y):
    global l
    visited = set()
    queue = deque([(start_x, start_y, 0)])
    while queue:
        x, y, depth = queue.popleft()
        if (x, y) == (des_x, des_y):
            return depth
        if (x, y) not in visited:
            visited.add((x, y))
            for i in a1:
                for j in a2:
                    x1, y1 = x + i, y + j
                    x2, y2 = x + j, y + i
                    if 0 <= x1 < l and 0 <= y1 < l and (x1, y1):
                        queue.append((x1, y1, depth + 1))
                    if 0 <= x2 < l and 0 <= y2 < l and (x2, y2):
                        queue.append((x2, y2, depth + 1))
    return 0


for _ in range(int(sys.stdin.readline().strip())):
    l = int(sys.stdin.readline().strip())
    now_x, now_y = map(int, sys.stdin.readline().strip().split())
    des_x, des_y = map(int, sys.stdin.readline().strip().split())
    result = bfs(now_x, now_y, des_x, des_y)
    print(result)
