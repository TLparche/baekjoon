import sys

n, s = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))

left = 0
right = 0
res = float('inf')
temp = numbers[0]
while right < n:
    if temp >= s:
        res = min(res, right - left + 1)
        temp -= numbers[left]
        left += 1
    else:
        if not right + 1 >= n:
            temp += numbers[right + 1]
        right += 1
if res == float('inf'):
    res = 0
print(res)
