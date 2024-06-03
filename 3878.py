import sys

input = sys.stdin.readline


def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])


def intersect(p1, p2, q1, q2):
    ccw1 = ccw(p1, p2, q1)
    ccw2 = ccw(p1, p2, q2)
    ccw3 = ccw(q1, q2, p1)
    ccw4 = ccw(q1, q2, p2)

    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if min(p1[0], p2[0]) > max(q1[0], q2[0]) or max(p1[0], p2[0]) < min(q1[0], q2[0]) \
                or min(p1[1], p2[1]) > max(q1[1], q2[1]) or max(p1[1], p2[1]) < min(q1[1], q2[1]):
            return False
        return True

    return ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0


def is_point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if min(p1y, p2y) < y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
                inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def do_polygons_intersect(polygon1, polygon2):
    for i in range(len(polygon1)):
        for j in range(len(polygon2)):
            if intersect(polygon1[i], polygon1[(i + 1) % len(polygon1)],
                         polygon2[j], polygon2[(j + 1) % len(polygon2)]):
                return True

    for point in polygon1:
        if is_point_in_polygon(point, polygon2):
            return True

    for point in polygon2:
        if is_point_in_polygon(point, polygon1):
            return True

    return False


def convex_hull(points):
    if len(points) <= 2:
        return points
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


for _ in range(int(input())):
    n, m = map(int, input().split())

    results = []
    black = [list(map(int, input().split())) for _ in range(n)]
    white = [list(map(int, input().split())) for _ in range(m)]

    if n == 1 and m == 1:
        print("YES")
    elif max(n, m) == 2 and min(n, m) == 1:
        if n > m:
            l, r = black, white
        else:
            l, r = white, black
        if min(l[0][0], l[1][0]) <= r[0][0] <= max(l[0][0], l[1][0]) and min(l[0][1], l[1][1]) <= r[0][1] <= max(
                l[0][1], l[1][1]) and ccw(l[0], l[1], r[0]) == 0:
            print("NO")
        else:
            print("YES")
    elif n == 2 and m == 2:
        if intersect(black[0], white[0], black[1], white[1]):
            print("YES")
        else:
            print("NO")
    else:
        convex_black = convex_hull(black)
        convex_white = convex_hull(white)
        if do_polygons_intersect(convex_black, convex_white):
            print("NO")
        else:
            print("YES")
