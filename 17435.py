import sys
import math

input = sys.stdin.readline

range_log = int(math.log2(500000))
m = int(input())
f = [0] + list(map(int, input().split()))
q = int(input())
dp = [[f[i]] for i in range(m + 1)]

for i in range(1, range_log + 1):
    for j in range(1, m + 1):
        dp[j].append(dp[dp[j][i - 1]][i - 1])

for _ in range(q):
    n, x = map(int, input().split())
    result = 0
    for i in range(range_log, -1, -1):
        if n >= 1 << i:
            n -= 1 << i
            x = dp[x][i]
    print(x)
