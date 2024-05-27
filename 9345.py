import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    tree = [[0, 0] for _ in range(2 * n)]
    for i in range(n):
        tree[n + i] = [i, i]

    for i in range(n - 1, 0, -1):
        tree[i][0] = min(tree[2 * i][0], tree[2 * i + 1][0])
        tree[i][1] = max(tree[2 * i][1], tree[2 * i + 1][1])

    for _ in range(k):
        query = list(map(int, input().split()))
        a, b = query[1], query[2]
        if query[0] == 0:
            tree[a + n], tree[b + n] = tree[b + n], tree[a + n]
            temp1, temp2 = a + n, b + n
            temp1 //= 2
            temp2 //= 2
            while temp1 or temp2:
                tree[temp1][0] = min(tree[2 * temp1][0], tree[2 * temp1 + 1][0])
                tree[temp1][1] = max(tree[2 * temp1][1], tree[2 * temp1 + 1][1])
                tree[temp2][0] = min(tree[2 * temp2][0], tree[2 * temp2 + 1][0])
                tree[temp2][1] = max(tree[2 * temp2][1], tree[2 * temp2 + 1][1])
                temp1 //= 2
                temp2 //= 2

        elif query[0] == 1:
            arrow_a = a + n
            arrow_b = b + n + 1
            is_correct = True

            while arrow_a < arrow_b:
                if arrow_a % 2:
                    if tree[arrow_a][0] < a or b < tree[arrow_a][1]:
                        is_correct = False
                        break
                    arrow_a += 1
                if arrow_b % 2:
                    arrow_b -= 1
                    if tree[arrow_b][0] < a or b < tree[arrow_b][1]:
                        is_correct = False
                arrow_a //= 2
                arrow_b //= 2

            if is_correct:
                print("YES")
            else:
                print("NO")
