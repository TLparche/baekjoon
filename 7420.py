import math
import sys

input = sys.stdin.readline


def distance_2d(u, v):
    u_x, u_y = u
    v_x, v_y = v
    return ((u_x - v_x) ** 2 + (u_y - v_y) ** 2) ** 0.5


def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])


def convex_hull(points):
    points.sort(key=lambda x: (x[0], x[1]))
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


n, l = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(n)]
convex = convex_hull(dots)

node_len = len(convex)
result = 0
for i in range(node_len):
    result += distance_2d(convex[(i + 1) % node_len], convex[i])
result += math.pi * l * 2
print(round(result))
