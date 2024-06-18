import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def update(tree, lazy, start, end, l, r, add, node):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[2 * node + 1] += lazy[node]
            lazy[2 * node + 2] += lazy[node]
        lazy[node] = 0

    if start > end or start > r or end < l:
        return

    if start >= l and end <= r:
        tree[node] += (end - start + 1) * add
        if start != end:
            lazy[2 * node + 1] += add
            lazy[2 * node + 2] += add
        return

    mid = (start + end) // 2
    update(tree, lazy, start, mid, l, r, add, 2 * node + 1)
    update(tree, lazy, mid + 1, end, l, r, add, 2 * node + 2)

    tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


def query_seg(tree, lazy, start, end, l, r, node):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[2 * node + 1] += lazy[node]
            lazy[2 * node + 2] += lazy[node]
        lazy[node] = 0

    if start > end or start > r or end < l:
        return 0

    if start >= l and end <= r:
        return tree[node]

    mid = (start + end) // 2
    left_sum = query_seg(tree, lazy, start, mid, l, r, 2 * node + 1)
    right_sum = query_seg(tree, lazy, mid + 1, end, l, r, 2 * node + 2)
    return left_sum + right_sum


def euler_tour(graph, start):
    visited = set()
    tour = []
    time = 0
    stack = deque([(start, True)])

    while stack:
        node, is_entry = stack.pop()

        if is_entry:
            if node not in visited:
                visited.add(node)
                tour.append(node)
                time += 1

                stack.append((node, False))
                for neighbor in reversed(graph[node]):
                    stack.append((neighbor, True))
        else:
            tour.append(node)
            time += 1

    return tour


n, m = map(int, input().split())
sellers = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(n):
    graph[sellers[i]].append(i + 1)

tour = euler_tour(graph, 1)
vector = [[-1, -1] for _ in range(n)]
ind = -1

for i in tour:
    i -= 1
    if vector[i][0] != -1:
        vector[i][1] = ind
    else:
        ind += 1
        vector[i][0] = ind

tree = [0] * (4 * n)
lazy = [0] * (4 * n)

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, b, c = query
        update(tree, lazy, 0, n - 1, vector[b - 1][0], vector[b - 1][1], c, 0)

    elif query[0] == 2:
        _, b = query
        result = query_seg(tree, lazy, 0, n - 1, vector[b - 1][0], vector[b - 1][0], 0)
        print(result)
