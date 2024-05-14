import sys

sys.setrecursionlimit(10 ** 9)


def preorder(in_start, in_end, post_start, post_end):
    global post_order, position
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    print(root, end=' ')

    left = position[root] - in_start
    right = in_end - position[root]

    preorder(in_start, position[root] - 1, post_start, post_start + left - 1)
    preorder(position[root] + 1, in_end, post_end - right, post_end - 1)


n = int(sys.stdin.readline().strip())
in_order = list(map(int, sys.stdin.readline().strip().split()))
post_order = list(map(int, sys.stdin.readline().strip().split()))
position = [0] * (n + 1)

for i in range(n):
    position[in_order[i]] = i

preorder(0, n - 1, 0, n - 1)
