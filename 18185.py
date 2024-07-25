import sys

input = sys.stdin.readline


def buy(ind, level):
    global a, result
    if level == 3:
        result += 3 * a[ind]
        a[ind] = 0

    elif level == 5:
        amount = min(a[ind:ind + 2])
        result += level * amount
        a[ind] -= amount
        a[ind + 1] -= amount

    else:
        amount = min(a[ind:ind + 3])
        result += level * amount
        a[ind] -= amount
        a[ind + 1] -= amount
        a[ind + 2] -= amount


n = int(input())
a = list(map(int, input().split())) + [0] * 2
result = 0

for i in range(n):
    if a[i] == 0:
        continue

    if a[i + 1] > a[i + 2]:
        amount = min(a[i], a[i + 1] - a[i + 2])
        result += 5 * amount
        a[i] -= amount
        a[i + 1] -= amount

        buy(i, 7)
        buy(i, 3)

    else:
        buy(i, 7)
        buy(i, 5)
        buy(i, 3)

print(result)
