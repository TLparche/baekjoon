import heapq
import sys


def dijkstra(k, tree):
    global n
    distance = [0] + [int(1e9) for _ in range(n)]
    heap = []
    heapq.heappush(heap, (0, k))
    while heap:
        length, node = heapq.heappop(heap)
        if distance[node] > length:
            distance[node] = length
            if node in tree:
                for a, b in tree[node]:
                    heapq.heappush(heap, (b + length, a))
    return distance


for _ in range(int(sys.stdin.readline().strip())):
    n, m, t = map(int, sys.stdin.readline().strip().split())
    s, g, h = map(int, sys.stdin.readline().strip().split())
    tree = {}
    destination = []
    road_length = 0
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().strip().split())
        if a == g and b == h:
            road_length = d
        elif a == h and b == g:
            road_length = d
        if a in tree:
            tree[a].append((b, d))
        else:
            tree[a] = [(b, d)]
        if b in tree:
            tree[b].append((a, d))
        else:
            tree[b] = [(a, d)]
    for _ in range(t):
        destination.append(int(sys.stdin.readline().strip()))

    start_route = dijkstra(s, tree)
    h_route = dijkstra(h, tree)
    g_route = dijkstra(g, tree)

    result = []

    for i in destination:
        if start_route[g] + road_length + h_route[i] == start_route[i]:
            result.append(i)
        elif start_route[h] + road_length + g_route[i] == start_route[i]:
            result.append(i)
    result.sort()
    print(*result)
