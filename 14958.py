import sys
import math

input = sys.stdin.readline


def power(a, b, mod):
    result = 1
    while b:
        if b % 2:
            result *= a
            result %= mod
        b //= 2
        a *= a
        a %= mod
    return result


def reverse_bit(a, n):
    result = [0] * n
    num_bits = n.bit_length() - 1
    for i in range(n):
        rev_i = 0
        for j in range(num_bits):
            if i & (1 << j):
                rev_i |= 1 << (num_bits - 1 - j)
        result[rev_i] = a[i]
    return result


def ntt(bit_arr, g, p, inv=False):
    len_bit = len(bit_arr)
    rev_bit_arr = reverse_bit(bit_arr, len_bit)

    block_size = 2
    while block_size <= len_bit:
        w_len = power(g, p // block_size, p)
        if inv:
            w_len = power(w_len, p - 2, p)
        for k in range(0, len_bit, block_size):
            w = 1
            for j in range(block_size // 2):
                t = (w % p) * rev_bit_arr[k + j + block_size // 2]
                u = rev_bit_arr[k + j]
                rev_bit_arr[k + j] = (u + t) % p
                rev_bit_arr[k + j + block_size // 2] = (u - t) % p
                w *= w_len
                w %= p
        block_size *= 2

    if inv:
        temp = p - (p - 1) // len_bit
        for i in range(len_bit):
            rev_bit_arr[i] = (rev_bit_arr[i] * temp) % p
    return rev_bit_arr


g = 3
p = 998244353
n, m = map(int, input().split())
ori_1 = input().strip()
ori_2 = input().strip()
u1, u2, u3 = [0] * n, [0] * n, [0] * n
d1, d2, d3 = [0] * m, [0] * m, [0] * m

for i in range(n):
    if ori_1[i] == "R":
        u1[i] = 1
    elif ori_1[i] == "S":
        u2[i] = 1
    else:
        u3[i] = 1

for i in range(m):
    if ori_2[i] == "P":
        d1[m - i - 1] = 1
    elif ori_2[i] == "R":
        d2[m - i - 1] = 1
    else:
        d3[m - i - 1] = 1

n_ntt = n + m - 1
n_padded = 1 << n_ntt.bit_length()
u1 += [0] * (n_padded - n)
u2 += [0] * (n_padded - n)
u3 += [0] * (n_padded - n)
d1 += [0] * (n_padded - m)
d2 += [0] * (n_padded - m)
d3 += [0] * (n_padded - m)

u1_ntt = ntt(u1, g, p)
u2_ntt = ntt(u2, g, p)
u3_ntt = ntt(u3, g, p)
d1_ntt = ntt(d1, g, p)
d2_ntt = ntt(d2, g, p)
d3_ntt = ntt(d3, g, p)

for i in range(len(u1_ntt)):
    u1_ntt[i] = (u1_ntt[i] * d1_ntt[i]) % p
    u2_ntt[i] = (u2_ntt[i] * d2_ntt[i]) % p
    u3_ntt[i] = (u3_ntt[i] * d3_ntt[i]) % p

u1_ntt = ntt(u1_ntt, g, p, True)
u2_ntt = ntt(u2_ntt, g, p, True)
u3_ntt = ntt(u3_ntt, g, p, True)

count = 0
for i in range(m - 1, len(u1_ntt)):
    count = max(count, u1_ntt[i] + u2_ntt[i] + u3_ntt[i])

print(count)
