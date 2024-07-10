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


x, y = input().split()
a = []
b = []
for i in range(len(x) - 1, -1, -1):
    a.append(int(x[i]))

for i in range(len(y) - 1, -1, -1):
    b.append(int(y[i]))

n_fft = len(a) + len(b) - 1
n_padded = 1 << n_fft.bit_length()
a += [0] * (n_padded - len(a))
b += [0] * (n_padded - len(b))

a_fft = fft(a)
b_fft = fft(b)
c_fft = [a_fft[i] * b_fft[i] for i in range(len(a_fft))]

res = ifft(c_fft)
ans = 0

for i in range(len(res)):
    ans += int(res[i].real + 0.5) * 10 ** i
print(ans)
