import sys

input = sys.stdin.readline


def buy_one(ind, level):
    global a, result
    result += level * a[ind]
    a[ind] = 0


def buy_two(ind, level):
    global a, result
    amount = min(a[ind:ind + 2])
    result += level * amount
    a[ind] -= amount
    a[ind + 1] -= amount


def buy_three(ind, level):
    global a, result
    amount = min(a[ind:ind + 3])
    result += level * amount
    a[ind] -= amount
    a[ind + 1] -= amount
    a[ind + 2] -= amount


n, b, c = map(int, input().split())
a = list(map(int, input().split())) + [0] * 2

if c > b:
    print(sum(a) * b)

else:
    result = 0
    for i in range(n):
        if a[i] == 0:
            continue

        if a[i + 1] > a[i + 2]:
            amount = min(a[i], a[i + 1] - a[i + 2])
            result += (b + c) * amount
            a[i] -= amount
            a[i + 1] -= amount

            buy_three(i, b + 2 * c)
            buy_one(i, b)
        else:
            buy_three(i, b + 2 * c)
            buy_two(i, b + c)
            buy_one(i, b)

    print(result)
