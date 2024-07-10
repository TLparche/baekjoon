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


upper = [0] * 60001
down = [0] * 60001
n1 = int(input())
X1 = list(map(int, input().split()))
n2 = int(input())
X2 = list(map(int, input().split()))
n3 = int(input())
X3 = list(map(int, input().split()))
for i in X1:
    upper[i + 30000] = 1
for i in X3:
    down[i + 30000] = 1

n_fft = 120001
n_padded = 1 << n_fft.bit_length()
upper += [0] * (n_padded - len(upper))
down += [0] * (n_padded - len(down))

upper_fft = fft(upper)
down_fft = fft(down)

C_fft = [upper_fft[i] * down_fft[i] for i in range(len(upper_fft))]
res = ifft(C_fft)
ans = 0

for i in X2:
    temp = int(res[2 * (i + 30000)].real + 0.5)
    if temp:
        ans += temp

print(ans)
