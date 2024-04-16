import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
LIS = [0]
for i in range(n):
    if a[i] > LIS[-1]:
        LIS.append(a[i])
    else:
        left = 0
        right = len(LIS) - 1
        while left <= right:
            cent = (left + right) // 2
            if LIS[cent] >= a[i]:
                right = cent - 1
            else:
                left = cent + 1
        LIS[right + 1] = a[i]
print(len(LIS) - 1)
