import sys


def length_cal(base):
    global router
    result = 1
    temp = router[0]
    for i in router:
        if i - temp >= base:
            result += 1
            temp = i
    return result


def binary_search(left, right):
    global c
    if left > right:
        print(right)
        return
    cent = (left + right) // 2
    result = length_cal(cent)

    if result >= c:
        return binary_search(cent + 1, right)
    else:
        return binary_search(left, cent - 1)


n, c = map(int, sys.stdin.readline().strip().split())
router = []
for _ in range(n):
    router.append(int(sys.stdin.readline().strip()))
router.sort()
binary_search(0, router[-1])
