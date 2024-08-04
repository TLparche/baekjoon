import sys
import math

input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    if n == 2:
        return True

    if n <= 1 or n % 2 == 0:
        return False

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in primes:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True


def miller_rabin(n, a):
    d = n - 1
    while d % 2 == 0:
        x = pow(a, d, n)
        if x == n - 1:
            return True
        elif x == 1:
            d //= 2
        else:
            return False

    l = pow(a, d, n)
    return l == 1 or l == n - 1


def g(x, n):
    return ((x * x) + 1) % n


def pollards_rho(n, x=2):
    p = x + 1
    if is_prime(n):
        return n
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if n % i == 0:
                return i
        y = x
        d = 1
        while d == 1:
            x = g(x, n)
            y = g(g(y, n), n)
            d = gcd(abs(x - y), n)
        if x % n == y % n:
            return pollards_rho(n, p)
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


def generate_combinations(factors):
    primes = list(factors.keys())
    powers = [list(range(factors[p] + 1)) for p in primes]

    def backtrack(index, current_comb):
        if index == len(primes):
            result.append(math.prod(current_comb))
            return

        prime = primes[index]
        for power in powers[index]:
            backtrack(index + 1, current_comb + [prime ** power])

    result = []
    backtrack(0, [])
    return result


while True:
    n = int(input())
    if n == 0:
        break

    n_str = str(n)
    if len(n_str) % 2:
        print(n_str + ": no")
        continue

    n_arr = [0] * 10
    for i in n_str:
        n_arr[int(i)] += 1

    len_comp = len(n_str) // 2
    factors = factorize(n)
    divisors = generate_combinations(factors)
    result = False
    divisors.sort()

    for i in divisors:
        if len(str(i)) != len_comp or len(str(n // i)) != len_comp:
            continue

        double_zero = False
        temp = [0] * 10
        last = "1"
        for j in str(i):
            temp[int(j)] += 1
            if last == j and last == "0":
                double_zero = True
                break
            last = j

        last = "1"
        for j in str(n // i):
            temp[int(j)] += 1
            if last == j and last == "0":
                double_zero = True
                break
            last = j

        if double_zero:
            continue
        if i % 10 == 0 and (n // i) % 10 == 0:
            continue

        if n_arr == temp:
            result = True
            break

    if result:
        print(n_str + ": yes")
    else:
        print(n_str + ": no")
