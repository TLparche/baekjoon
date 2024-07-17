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
n = int(input())
left = [0] * n  # 나머지 i인 제곱수 개수
check = {}  # a==b 제곱수 개수
check_ind = set()  # 합성곱 이후 체크할 인덱스 집합

for i in range(1, n):
    ind = (i ** 2) % n  # 제곱수 나머지
    left[ind] += 1
    check_ind.add(ind)
    check_ind.add(ind + n)
    if (ind * 2) % n not in check:
        check[(ind * 2) % n] = 1
    else:
        check[(ind * 2) % n] += 1

n_ntt = 2 * n - 1
n_padded = 1 << n_ntt.bit_length()
left += [0] * (n_padded - n)

left_ntt = ntt(left, g, p)

for i in range(len(left_ntt)):
    left_ntt[i] = (left_ntt[i] * left_ntt[i]) % p

left_ntt = ntt(left_ntt, g, p, True)
res_set = {}  # 각 나머지에 몇개 있는지

for i in check_ind:
    temp = left_ntt[i]
    if temp:
        if i % n not in res_set:
            res_set[i % n] = temp
        else:
            res_set[i % n] += temp

for i in check:
    if i in res_set:
        res_set[i] += check[i]

ans = 0
for i in res_set:
    ans += (res_set[i] // 2) * left[i]

print(ans)
