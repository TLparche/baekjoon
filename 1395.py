import sys

input = sys.stdin.readline


def init_seg(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        init_seg(arr, tree, start, mid, 2 * node + 1)
        init_seg(arr, tree, mid + 1, end, 2 * node + 2)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


def update(tree, tree_num, lazy, start, end, l, r, node):
    if lazy[node] != 0:
        if lazy[node] % 2:
            tree[node] = tree_num[node] - tree[node]
        if start != end:
            lazy[2 * node + 1] += lazy[node]
            lazy[2 * node + 2] += lazy[node]
        lazy[node] = 0

    if start > end or start > r or end < l:
        return

    if start >= l and end <= r:
        tree[node] = tree_num[node] - tree[node]
        if start != end:
            lazy[2 * node + 1] += 1
            lazy[2 * node + 2] += 1
        return

    mid = (start + end) // 2
    update(tree, tree_num, lazy, start, mid, l, r, 2 * node + 1)
    update(tree, tree_num, lazy, mid + 1, end, l, r, 2 * node + 2)

    tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


def query_seg(tree, lazy, start, end, l, r, node):
    if lazy[node] != 0:
        if lazy[node] % 2:
            tree[node] = tree_num[node] - tree[node]
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


n, m = map(int, input().split())

tree = [0] * (4 * n)
tree_num = [0] * (4 * n)
lazy = [0] * (4 * n)
numbers = [1 for _ in range(n)]
init_seg(numbers, tree_num, 0, n - 1, 0)

for _ in range(m):
    o, s, t = map(int, input().split())
    if o == 0:
        update(tree, tree_num, lazy, 0, n - 1, s - 1, t - 1, 0)

    elif o == 1:
        result = query_seg(tree, lazy, 0, n - 1, s - 1, t - 1, 0)
        print(result)
