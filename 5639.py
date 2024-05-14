import sys

sys.setrecursionlimit(10 ** 9)


def in_order(tree):
    if len(tree) == 0:
        return

    root = tree[0]
    left = []
    right = []
    for i in range(1, len(tree)):
        if tree[i] > root:
            left = tree[1:i]
            right = tree[i:]
            break
    else:
        left = tree[1:]

    in_order(left)
    in_order(right)
    print(root)


post_order = []
while True:
    try:
        n = int(sys.stdin.readline().strip())
        post_order.append(n)
    except:
        break

in_order(post_order)
