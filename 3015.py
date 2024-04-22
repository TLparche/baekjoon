import sys

n = int(sys.stdin.readline().strip())
a = [int(sys.stdin.readline().strip()) for _ in range(n)]
result = [0] * n
stack = [[a[0], 1]]

for i in range(1, n):
    while stack and stack[-1][0] < a[i]:
        result[i] += stack.pop()[1]
    if not stack:
        stack.append([a[i], 1])
    elif stack[-1][0] == a[i]:
        count = stack.pop()[1]
        result[i] += count
        if stack:
            result[i] += 1
        stack.append([a[i], count + 1])
    else:
        stack.append([a[i], 1])
        result[i] += 1

print(sum(result))
