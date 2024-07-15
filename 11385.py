import sys

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


def conv(left, right, g, p):
    a_ntt = ntt(left, g, p)
    b_ntt = ntt(right, g, p)
    c_ntt = [(a_ntt[i] * b_ntt[i]) % p for i in range(len(a_ntt))]
    c_ntt = ntt(c_ntt, g, p, True)
    return c_ntt


def main():
    g = 3
    p1 = 998244353
    p2 = 2281701377
    p1_inv = 253522377
    p2_inv = 887328313

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    n_ntt = n + m + 1
    n_padded = 1 << n_ntt.bit_length()
    a += [0] * (n_padded - n - 1)
    b += [0] * (n_padded - m - 1)

    res1 = conv(a, b, g, p1)
    res2 = conv(a, b, g, p2)

    ans = 0
    for i, j in zip(res1, res2):
        ans ^= (i * p2 * p2_inv + j * p1 * p1_inv) % (p1 * p2)

    print(ans)


main()
