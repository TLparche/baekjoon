import sys

input = sys.stdin.readline

n, m = map(int, input().split())

customer = [[0, 0] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    customer[i][0] = a
    customer[i][1] = b
customer.sort(key=lambda x: x[1])

temp = [customer[0][1], customer[0][0]]
res = 0
for j, i in customer:
    if i < j:
        if temp[1] < i:
            res += temp[1] - temp[0]
            temp = [i, j]
        else:
            temp[1] = max(temp[1], j)
res += temp[1] - temp[0]
print(m + res * 2)
