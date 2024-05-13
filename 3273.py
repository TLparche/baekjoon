import sys

n = int(sys.stdin.readline().strip())
numbers = sorted(list(map(int, sys.stdin.readline().strip().split())))
x = int(sys.stdin.readline().strip())

ans = 0
left, right = 0, n-1
while left < right:
    temp = numbers[left] + numbers[right]
    if temp == x:
        ans += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(ans)