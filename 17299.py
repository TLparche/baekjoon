import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
result = [-1] * n
stack = [0]
count = {}
for i in a:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for i in range(1, n):
    while stack and count[a[stack[-1]]] < count[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)
