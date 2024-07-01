import sys
import math

input = sys.stdin.readline


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def binomial_coefficient(n, k):
    if n < k:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def convert(a, m):
    conv = []
    while a > 0:
        a, remainder = divmod(a, m)
        conv.append(remainder)

    return conv[::-1]


def get_binomial_coefficient(n, k, mod):
    conv_n = convert(n, mod)
    conv_k = convert(k, mod)

    while len(conv_n) > len(conv_k):
        conv_k.insert(0, 0)
    while len(conv_k) > len(conv_n):
        conv_n.insert(0, 0)

    result = 1
    for i in range(len(conv_k)):
        if conv_n[i] < conv_k[i]:
            result = 0
            break
        result *= binomial_coefficient(conv_n[i], conv_k[i])
    result %= mod
    return result


for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 0:
        print(1)
        continue
    if k > n:
        k = 2 * n - k
    result = 0
    for j in range(math.floor(k / 2) + 1):
        result += (get_binomial_coefficient(n, j, 3) * get_binomial_coefficient(n - j, k - 2 * j, 3)) % 3
        result %= 3

    print(result)
