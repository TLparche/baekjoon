import heapq
import sys

v, e = map(int, sys.stdin.readline().strip().split())
k = int(sys.stdin.readline().strip())
tree = {}
distance = [0] + [float("inf") for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a in tree:
        tree[a].append((b, c))
    else:
        tree[a] = [(b, c)]
heap = []
heapq.heappush(heap, (0, k))
while heap:
    length, node = heapq.heappop(heap)
    if distance[node] > length:
        distance[node] = length
        if node in tree:
            for a, b in tree[node]:
                heapq.heappush(heap, (b + length, a))
for i in range(v):
    temp = distance[i + 1]
    if temp == float("inf"):
        print("INF")
    else:
        print(temp)
