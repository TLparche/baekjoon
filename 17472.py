import sys
from collections import deque

input = sys.stdin.readline


def find(node, root_node):
    if node != root_node[node]:
        root_node[node] = find(root_node[node], root_node)
    return root_node[node]


def union(root, child, root_node):
    l_root = find(root, root_node)
    r_root = find(child, root_node)
    if l_root != r_root:
        root_node[r_root] = l_root


def bridge_bfs(matrix, start, cur):
    global directions, route
    rows, cols = len(matrix), len(matrix[0])
    queue = deque()
    x, y = start
    for i in directions:
        queue.append((x, y, i, 0))

    while queue:
        ax, ay, dir, length = queue.popleft()

        nx, ny = ax + dir[0], ay + dir[1]
        if not (0 <= nx < rows and 0 <= ny < cols):
            continue
        if matrix[nx][ny] == cur:
            continue
        if matrix[nx][ny] != 0:
            if length >= 2:
                route.append([cur, matrix[nx][ny], length])
            continue

        queue.append((nx, ny, dir, length + 1))


def island_bfs(matrix, start, index):
    global visited, directions
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if visited[x][y] != 0:
            continue

        visited[x][y] = index

        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]

            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] == 1:
                queue.append((nx, ny))


island_map = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
route = []
n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
result = 0
for i in range(n):
    island_map.append(list(map(int, input().split())))
island_number = 1

for i in range(n):
    for j in range(m):
        if island_map[i][j] == 1 and visited[i][j] == 0:
            island_bfs(island_map, (i, j), island_number)
            island_number += 1

for i in range(n):
    for j in range(m):
        if island_map[i][j] != 0:
            bridge_bfs(visited, (i, j), visited[i][j])

root_node = [i for i in range(island_number)]
route.sort(key=lambda x: x[2])
route_num = 0
for cur in route:
    if find(cur[0], root_node) != find(cur[1], root_node):
        union(cur[0], cur[1], root_node)
        result += cur[2]
        route_num += 1

if route_num == island_number - 2:
    print(result)
else:
    print(-1)
