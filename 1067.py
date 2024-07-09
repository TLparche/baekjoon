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


n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X += X
Y.reverse()

n_fft = 2 * n + len(Y) - 1
n_padded = 1 << n_fft.bit_length()
X += [0] * (n_padded - len(X))
Y += [0] * (n_padded - len(Y))

X_fft = fft(X)
Y_fft = fft(Y)

for i in range(len(X_fft)):
    X_fft[i] *= Y_fft[i]

res = ifft(X_fft)
for i in range(len(res)):
    res[i] = int(res[i].real + 0.5)

print(max(res))
