import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def cal_distance(l, r):
    global case1, case2
    lx, ly = case1[l]
    rx, ry = case2[r]
    next = max(l, r) + 1
    len_l = abs(lx - case1[next][0]) + abs(ly - case1[next][1])
    len_r = abs(rx - case2[next][0]) + abs(ry - case2[next][1])
    return len_l, len_r, next


def find(l, r):
    global w, dp
    if l == w or r == w:
        return 0
    if dp[l][r] != -1:
        return dp[l][r]
    len_l, len_r, next = cal_distance(l, r)
    dp[l][r] = min(len_l + find(next, r), len_r + find(l, next))
    return dp[l][r]


def police(l, r):
    global w, dp
    if l == w or r == w:
        return
    len_l, len_r, next = cal_distance(l, r)
    if len_l + dp[next][r] < len_r + dp[l][next]:
        print(1)
        police(next, r)
    else:
        print(2)
        police(l, next)


n = int(input())
w = int(input())

case1 = [(1, 1)]
case2 = [(n, n)]
dp = [[-1 for _ in range(w + 1)] for _ in range(w + 1)]

for _ in range(w):
    x, y = map(int, input().split())
    case1.append((x, y))
    case2.append((x, y))

print(find(0, 0))
police(0, 0)
