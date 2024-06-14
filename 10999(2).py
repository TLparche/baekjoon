def init_seg(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        init_seg(arr, tree, start, mid, 2 * node + 1)
        init_seg(arr, tree, mid + 1, end, 2 * node + 2)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


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


n, m, k = map(int, input().split())

tree = [0] * (4 * n)
lazy = [0] * (4 * n)
numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

init_seg(numbers, tree, 0, n - 1, 0)

for _ in range(m + k):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, b, c, d = query
        update(tree, lazy, 0, n - 1, b - 1, c - 1, d, 0)

    elif query[0] == 2:
        _, b, c = query
        result = query_seg(tree, lazy, 0, n - 1, b - 1, c - 1, 0)
        print(result)
