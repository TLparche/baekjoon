import sys

input = sys.stdin.readline


def distance_2d(u, v):
    u_x, u_y = u
    v_x, v_y = v
    return ((u_x - v_x) ** 2 + (u_y - v_y) ** 2) ** 0.5


def distance(u, v):
    global convex, node_len
    up, down = 0, 0
    l, r = u, v
    while True:
        l %= node_len
        if l == v:
            break
        up += node_dist[l]
        l += 1
    while True:
        r %= node_len
        if r == u:
            break
        down += node_dist[r]
        r += 1
    return min(up, down)


def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])


def shift_ccw(p1, p2, p3, p4):
    return ccw(p1, p2, [p4[0] - p3[0] + p2[0], p4[1] - p3[1] + p2[1]])


n = int(input())
results = []
convex = [list(map(int, input().split())) for _ in range(n)]
convex = convex[::-1]

node_len = len(convex)
node_dist = []
for i in range(node_len):
    node_dist.append(distance_2d(convex[(i + 1) % node_len], convex[i]))

dist = [0, 0, 0]
k = 1
for i in range(node_len):
    while True:
        if k + 1 == i:
            break
        if shift_ccw(convex[i], convex[(i + 1) % node_len], convex[k % node_len],
                     convex[(k + 1) % node_len]) <= 0:
            break
        dist_len = distance(i, k % node_len)
        if dist_len > dist[0]:
            dist = [dist_len, i, k % node_len]
        k += 1

    dist_len = distance(i, k % node_len)
    if dist_len > dist[0]:
        dist = [dist_len, i, k % node_len]
end_a = convex[dist[1]]
end_b = convex[dist[2]]

result = (dist[0], 0, 0)
ind = dist[1] + 1
while True:
    ind %= node_len
    if ind == dist[2]:
        break
    dist_new = distance_2d(convex[ind], convex[dist[1]])
    cur = ind
    while True:
        cur %= node_len
        if cur == dist[2]:
            break
        dist_new += node_dist[cur]
        cur += 1
    if dist_new < result[0]:
        result = (dist_new, dist[1], ind)
    ind += 1

ind = dist[2] + 1
while True:
    ind %= node_len
    if ind == dist[1]:
        break
    dist_new = distance_2d(convex[ind], convex[dist[2]])
    cur = ind
    while True:
        cur %= node_len
        if cur == dist[1]:
            break
        dist_new += node_dist[cur]
        cur += 1
    if dist_new < result[0]:
        result = (dist_new, dist[2], ind)
    ind += 1

print(*convex[result[1]], *convex[result[2]])
