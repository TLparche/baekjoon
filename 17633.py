import sys

input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(k):
    if k <= 97:
        return k in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    else:
        return all(miller_rabin(k, i) for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


def miller_rabin(n, a):
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


def g(x, n):
    return ((x * x) + 1) % n


def pollards_rho(n, x):
    p = x
    if is_prime(n):
        return n
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            if n % i == 0:
                return i
        y = x
        d = 1
        while d == 1:
            x = g(x, n)
            y = g(g(y, n), n)
            d = gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n, p + 1)
        else:
            if is_prime(d):
                return d
            else:
                return pollards_rho(d, 2)


def factorize(n):
    factors = {}
    while n != 1:
        k = pollards_rho(n, 2)
        if k not in factors:
            factors[k] = 1
        elif k in factors:
            factors[k] += 1
        n //= k
    return factors


def check_square(n):
    factors = factorize(n)

    if check_square_number(factors):
        return 1

    if fermat_two_squares(factors):
        return 2

    if legendre_three_squares(factors):
        return 3

    return 4


def check_square_number(factors):
    for i in factors:
        if factors[i] % 2 == 1:
            return False
    return True


def fermat_two_squares(factors):
    for i in factors:
        if i % 4 == 3:
            if factors[i] % 2 == 1:
                return False
    return True


def legendre_three_squares(factors):
    count = 1
    for i in factors:
        if i == 2:
            if factors[2] % 2 == 1:
                count *= 2
            continue

        count *= pow(i, factors[i], 8)
        count %= 8
    if count == 7:
        return False
    return True


a = int(input())
print(check_square(a))
