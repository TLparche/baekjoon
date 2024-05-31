import sys

input = sys.stdin.readline


def distance_line(a, b, c):
    A = c[1] - b[1]
    B = b[0] - c[0]
    C = -B * b[1] - A * b[0]
    return abs(A * a[0] + B * a[1] + C) / ((A ** 2 + B ** 2) ** 0.5)


def distance(u, v):
    u_x, u_y = u
    v_x, v_y = v
    return (u_x - v_x) ** 2 + (u_y - v_y) ** 2


def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])


def shift_ccw(p1, p2, p3, p4):
    return ccw(p1, p2, [p4[0] - p3[0] + p2[0], p4[1] - p3[1] + p2[1]])


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


n, r = map(int, input().split())
results = []
dots = [list(map(int, input().split())) for _ in range(n)]

convex = convex_hull(dots)
node_len = len(convex)

width = float("inf")
k = 1
for i in range(node_len):
    diagonal = 0
    while True:
        if k + 1 == i:
            break
        if shift_ccw(convex[i], convex[(i + 1) % node_len], convex[k % node_len],
                     convex[(k + 1) % node_len]) <= 0:
            break
        dist_len = distance_line(convex[k % node_len], convex[i], convex[(i + 1) % node_len])
        diagonal = max(diagonal, dist_len)
        k += 1

    dist_len = distance_line(convex[k % node_len], convex[i], convex[(i + 1) % node_len])
    diagonal = max(diagonal, dist_len)
    width = min(width, diagonal)
print(width)
