import heapq
import sys


def dijkstra(k, tree):
    distance = [0] + [float("inf") for _ in range(v)]
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


v, e = map(int, sys.stdin.readline().strip().split())
tree = {}
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a in tree:
        tree[a].append((b, c))
    else:
        tree[a] = [(b, c)]
    if b in tree:
        tree[b].append((a, c))
    else:
        tree[b] = [(a, c)]
v1, v2 = map(int, sys.stdin.readline().strip().split())

start_0 = dijkstra(1, tree)
start_1 = dijkstra(v1, tree)
start_2 = dijkstra(v2, tree)

route_1 = start_0[v1] + start_1[v2] + start_2[-1]
route_2 = start_0[v2] + start_2[v1] + start_1[-1]

result = min(route_1, route_2)
if result == float("inf"):
    print(-1)
else:
    print(result)
