import sys
from collections import deque


def dfs(start, graph):
    global visited
    queue = deque([(start, -1)])

    while queue:
        current, parrent = queue.popleft()
        if visited[current]:
            return True

        visited[current] = True
        for next in graph[current]:
            if not visited[next]:
                queue.append((next, current))
            elif next != parrent:
                return True

    return False


time = 1
while True:
    n, m = map(int, sys.stdin.readline().strip().split())
    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    result = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            if not dfs(i, tree):
                result += 1
    if result == 0:
        print("Case {}: No trees.".format(time))
    elif result == 1:
        print("Case {}: There is one tree.".format(time))
    else:
        print("Case {}: A forest of {} trees.".format(time, result))
    time += 1
