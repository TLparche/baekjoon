import sys

n, s = map(int, sys.stdin.readline().strip().split())
numbers = sorted(list(map(int, sys.stdin.readline().strip().split())))

left = 0
right = n - 1
ans = float('inf')
res = [0, 0]

while left < right:
    temp = numbers[left] + numbers[right]
    if abs(temp) < abs(ans):
        ans = temp
        res[0] = numbers[left]
        res[1] = numbers[right]
    if temp < 0:
        left += 1
    elif temp == 0:
        break
    else:
        right -= 1

print(*res)
