import sys
import math

input = sys.stdin.readline


def reverse_bit(x):
    len_x = len(x)
    j = 0
    for i in range(1, len_x):
        bit = len_x >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            x[i], x[j] = x[j], x[i]
    return x


def fft(bit_arr):
    len_bit = len(bit_arr)
    rev_bit_arr = reverse_bit(bit_arr)

    block_size = 2
    while block_size <= len_bit:
        wk = math.exp(1) ** (-2j * math.pi / block_size)  # 회전인자 처리하기
        for k in range(0, len_bit, block_size):
            w = 1
            for j in range(block_size // 2):
                t = w * rev_bit_arr[k + j + block_size // 2]
                u = rev_bit_arr[k + j]
                rev_bit_arr[k + j] = u + t
                rev_bit_arr[k + j + block_size // 2] = u - t
                w *= wk
        block_size *= 2
    return rev_bit_arr


def ifft(bit):
    conj_bit = [i.conjugate() for i in bit]
    conj_bit = fft(conj_bit)
    bit = [i.conjugate() / len(bit) for i in conj_bit]
    return bit


max = 5 * 10 ** 5
a = [0] + [1] * max
p = 3

while p ** 2 <= 10 ** 6:
    if a[(p - 1) // 2]:
        for i in range(p ** 2, 10 ** 6 + 1, 2 * p):
            a[(i - 1) // 2] = 0
    p += 2

n_fft = 2 * len(a) - 1
n_padded = 1 << n_fft.bit_length()
a += [0] * (n_padded - len(a))

a_fft = fft(a)
b_fft = [a_fft[i] ** 2 for i in range(len(a_fft))]

res = ifft(b_fft)

for _ in range(int(input())):
    n = int(input())
    if n == 4:
        print(1)
        continue
    temp = int(res[n // 2 - 1].real + 0.5)

    if temp % 2:
        temp += 1
    temp //= 2
    print(temp)
