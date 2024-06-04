import sys
import math

input = sys.stdin.readline

s, p = map(int, input().split())
log_p = math.log(p)
prev = -1
n = 2

if s == p:
    print(1)
else:
    while True:
        now = n * math.log(s / n)
        if now < prev:
            print(-1)
            break
        if log_p <= now:
            print(n)
            break
        prev = now
        n += 1
