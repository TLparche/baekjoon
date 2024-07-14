import sys
import math

input = sys.stdin.readline


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


def fft(bit_arr):
    len_bit = len(bit_arr)
    rev_bit_arr = reverse_bit(bit_arr, len_bit)

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
    temp = [1 if (i.conjugate() / len(bit)).real > 0.5 else 0 for i in conj_bit]
    return temp[:next((i for i in range(len(temp) - 1, -1, -1) if temp[i] == 1), None) + 1] if any(temp) else temp


def divide_conquer(k, a):
    if k == 1:
        return a
    if k % 2:
        left = divide_conquer((k - 1) // 2, a)
        left, right = fft_calc(left, a, 1)
        return ifft([left[i] * left[i] * right[i] for i in range(len(left))])

    else:
        left = divide_conquer(k // 2, a)
        left = fft_calc(left, left, 0)
        return ifft([left[i] * left[i] for i in range(len(left))])


def fft_calc(left, right, check):
    if check == 0:
        n_fft = len(left) + len(right) - 1
        n_padded = 1 << n_fft.bit_length()
        left += [0] * (n_padded - len(left))
        left_fft = fft(left)

        return left_fft

    else:
        n_fft = len(left) * 2 + len(right) - 2
        n_padded = 1 << n_fft.bit_length()
        left += [0] * (n_padded - len(left))
        left_fft = fft(left)
        right += [0] * (n_padded - len(right))
        right_fft = fft(right)

        return left_fft, right_fft


def main():
    n, k = map(int, input().split())
    temp = list(map(int, input().split()))
    a = [0] * 1001

    for i in temp:
        a[i] = 1

    res = divide_conquer(k, a)

    for i in range(len(res)):
        if res[i]:
            print(i, end=" ")


main()
