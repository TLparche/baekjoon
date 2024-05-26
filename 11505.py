import sys

input = sys.stdin.readline

mod = 1000000007

n, m, k = map(int, input().split())
numbers = []
for i in range(n):
    numbers.append(int(input()))

tree = [0] * (2 * n)
for i in range(n):
    tree[n + i] = numbers[i] % mod

for i in range(n - 1, 0, -1):
    tree[i] = (tree[2 * i] * tree[2 * i + 1]) % mod

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        ori = numbers[b - 1]
        numbers[b - 1] = c % mod
        temp = n + b - 1
        while temp:
            if 2 * temp + 1 < 2 * n:
                tree[temp] = (tree[2 * temp] * tree[2 * temp + 1]) % mod
            else:
                tree[temp] = c % mod
            if temp % 2:
                temp -= 1
            temp //= 2
    else:
        result = 1
        b += n - 1
        c += n
        while b < c:
            if b % 2:
                result *= tree[b]
                b += 1
            if c % 2:
                c -= 1
                result *= tree[c]
            result %= mod
            b //= 2
            c //= 2
        print(result % mod)
