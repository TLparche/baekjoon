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
ori = input().strip()
ori_len = len(ori)
a, b = [0] * ori_len, [0] * ori_len
for i in range(ori_len):
    if ori[i] == 'A':
        a[i] = 1
    else:
        b[ori_len - i - 1] = 1

n_ntt = 2 * ori_len - 1
n_padded = 1 << n_ntt.bit_length()
a += [0] * (n_padded - ori_len)
b += [0] * (n_padded - ori_len)

a_ntt = ntt(a, g, p)
b_ntt = ntt(b, g, p)

for i in range(len(a_ntt)):
    a_ntt[i] = (a_ntt[i] * b_ntt[i]) % p

a_ntt = ntt(a_ntt, g, p, True)
for i in a_ntt[n_ntt - ori_len + 1:n_ntt]:
    print(i)
