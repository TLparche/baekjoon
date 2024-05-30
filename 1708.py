import sys

input = sys.stdin.readline


def cross_product_2d(u, v):
    u_x, u_y = u
    v_x, v_y = v
    return u_x * v_y - u_y * v_x


def make_dorm(arr, way):
    global dots
    for i in range(1, len(dots)):
        if len(arr) == 1:
            arr.append(dots[i])
            continue
        temp = cross_product_2d([arr[-1][0] - arr[-2][0], arr[-1][1] - arr[-2][1]],
                                [dots[i][0] - arr[-1][0], dots[i][1] - arr[-1][1]])

        if (way and temp < 0) or (not way and temp > 0):
            arr.append(dots[i])
        else:
            while (way and temp >= 0) or (not way and temp <= 0):
                arr.pop()
                if len(arr) == 1:
                    break
                temp = cross_product_2d([arr[-1][0] - arr[-2][0], arr[-1][1] - arr[-2][1]],
                                        [dots[i][0] - arr[-1][0], dots[i][1] - arr[-1][1]])
            arr.append(dots[i])
    return arr


n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

dots.sort(key=lambda x: (x[0], x[1]))

upper = [dots[0]]
lower = [dots[0]]
upper = make_dorm(upper, True)
lower = make_dorm(lower, False)

print(len(upper) + len(lower) - 2)
