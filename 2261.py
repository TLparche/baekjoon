import sys

input = sys.stdin.readline


def calc_dist(a, b):
    ax, ay = a
    bx, by = b
    return (ax - bx) ** 2 + (ay - by) ** 2


def min_dist_calc(left, right):
    if left == right:
        return float("inf")

    elif right - left == 1:
        return calc_dist(loca[left], loca[right])

    mid = (left + right) // 2
    min_dis = min(min_dist_calc(left, mid), min_dist_calc(mid + 1, right))

    temp = []
    for i in range(left, right + 1):
        if (loca[i][0] - loca[mid][0]) ** 2 < min_dis:
            temp.append(loca[i])

    temp.sort(key=lambda x: x[1])

    for i in range(len(temp) - 1):
        for j in range(i + 1, len(temp)):
            if (temp[i][1] - temp[j][1]) ** 2 < min_dis:
                min_dis = min(min_dis, calc_dist(temp[i], temp[j]))
            else:
                break
    return min_dis


n = int(input())
loca = []
for _ in range(n):
    loca.append(list(map(int, input().split())))

loca.sort(key=lambda x: (x[0], x[1]))

res = min_dist_calc(0, n - 1)
print(res)
