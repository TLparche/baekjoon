import sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(m):
        _, _ = sys.stdin.readline().split()
    print(n - 1)
