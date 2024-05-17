import math
import sys

input = sys.stdin.readline

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if abs(r1 - r2) < d < r1 + r2:
    alpha = 2 * math.acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1))
    beta = 2 * math.acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2))
    result = (r1 ** 2 * (alpha - math.sin(alpha)) + r2 ** 2 * (beta - math.sin(beta))) * 0.5
    print(round(result, 3))
elif d <= abs(r1 - r2):
    result = math.pi * min(r1, r2) ** 2
    print(round(result, 3))
else:
    print("0.000")
