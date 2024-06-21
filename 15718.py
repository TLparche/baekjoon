import sys

input = sys.stdin.readline


def mod_inverse(r1, r2):
    p = r1
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r

        s = s1 - q * s2
        s1, s2 = s2, s

        t = t1 - q * t2
        t1, t2 = t2, t

    if t1 < 0:
        t1 += p
    return t1


def make_arr(a, m):
    conv = []
    while a > 0:
        a, remainder = divmod(a, m)
        conv.append(remainder)

    return conv[::-1]


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


def part_binomial_coefficient(n, m, mod):
    arr_a = make_arr(n - 1, mod)
    arr_b = make_arr(m - 2, mod)

    while len(arr_a) > len(arr_b):
        arr_b.insert(0, 0)

    while len(arr_b) > len(arr_a):
        arr_a.insert(0, 0)

    result = 1
    for i in range(len(arr_b)):
        if arr_a[i] < arr_b[i]:
            result = 0
            break
        result *= binomial_coefficient(arr_a[i], arr_b[i])
    return result % mod


mod_a = 1031
mod_b = 97

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1 and m > 2:
        print(0)
        continue
    if n == 0 and m == 1:
        print(1)
        continue
    if n == 0:
        print(0)
        continue
    if m == 1:
        print(0)
        continue

    part_a = part_binomial_coefficient(n, m, mod_a)
    part_b = part_binomial_coefficient(n, m, mod_b)

    mod_c = mod_a * mod_b
    inv_mod_a = mod_inverse(mod_a, mod_b) % mod_c
    inv_mod_b = mod_inverse(mod_b, mod_a) % mod_c

    result = (mod_b * inv_mod_a * part_a + mod_a * inv_mod_b * part_b) % mod_c
    print(result)
