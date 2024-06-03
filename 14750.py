import sys
from collections import deque

input = sys.stdin.readline


def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])


def is_point_on_segment(p, seg_start, seg_end):
    return min(seg_start[0], seg_end[0]) <= p[0] <= max(seg_start[0], seg_end[0]) and \
        min(seg_start[1], seg_end[1]) <= p[1] <= max(seg_start[1], seg_end[1])


def intersect(p1, p2, q1, q2):
    ccw1 = ccw(p1, p2, q1)
    ccw2 = ccw(p1, p2, q2)
    ccw3 = ccw(q1, q2, p1)
    ccw4 = ccw(q1, q2, p2)

    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if min(p1[0], p2[0]) > max(q1[0], q2[0]) or max(p1[0], p2[0]) < min(q1[0], q2[0]) \
                or min(p1[1], p2[1]) > max(q1[1], q2[1]) or max(p1[1], p2[1]) < min(q1[1], q2[1]):
            return False
        return True
    return ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0


def wall_intersect(walls, mouse, hole):
    temp = 0
    for wall in walls:
        if hole == wall[0] or hole == wall[1]:
            continue
        if intersect(mouse, hole, wall[0], wall[1]):
            temp += 1
    if temp <= 1:
        return True
    return False


def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == sink:
                    return True
    return False


def edmonds_karp(graph, source, sink):
    copy_graph = [row[:] for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(copy_graph, source, sink, parent):
        path_flow = float('Inf')
        cur = sink

        while cur != source:
            path_flow = min(path_flow, copy_graph[parent[cur]][cur])
            cur = parent[cur]

        max_flow += path_flow

        cur = sink
        while cur != source:
            cur_parent = parent[cur]
            copy_graph[cur_parent][cur] -= path_flow
            copy_graph[cur][cur_parent] += path_flow
            cur = parent[cur]
        parent = [-1] * len(graph)
    return max_flow


n, k, h, m = map(int, input().split())
frame = []
for _ in range(n):
    frame.append(list(map(int, input().split())))

holes = []
for _ in range(h):
    holes.append(list(map(int, input().split())))

mices = []
for _ in range(m):
    mices.append(list(map(int, input().split())))

walls = []
for i in range(n):
    cur = i
    next = (i + 1) % n
    walls.append((frame[cur], frame[next]))

graph = [[0 for _ in range(h + m + 2)] for _ in range(h + m + 2)]
for i in range(1, m + 1):
    graph[0][i] = 1

for i in range(1, m + 1):
    for j in range(1, h + 1):
        if wall_intersect(walls, mices[i - 1], holes[j - 1]):
            graph[i][j + m] = 1

for i in range(1, h + 1):
    graph[m + i][h + m + 1] = k

if m == edmonds_karp(graph, 0, h + m + 1):
    print('Possible')
else:
    print('Impossible')
