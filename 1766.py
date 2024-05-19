import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
height = [0] * (n + 1)
graph = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    height[b] += 1

heap = []
for i in range(1, n + 1):
    if height[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    node = heapq.heappop(heap)
    result.append(node)
    if node in graph:
        for friend in graph[node]:
            height[friend] -= 1
            if height[friend] == 0:
                heapq.heappush(heap, friend)

print(*result)
