import math
import sys

input = sys.stdin.readline

n = int(input())
graph = [0 for _ in range(4 * 10 ** 6)]


def put_candy(left, right, node, taste, amount):
    mid = (left + right) // 2
    graph[node] += amount
    if left == right:
        return
    if taste <= mid:
        put_candy(left, mid, node * 2, taste, amount)
    else:
        put_candy(mid + 1, right, node * 2 + 1, taste, amount)


def take_candy(left, right, node, level):
    mid = (left + right) // 2
    graph[node] -= 1
    if left == right:
        return mid

    amount = graph[node * 2]
    if amount >= level:
        return take_candy(left, mid, node * 2, level)
    else:
        return take_candy(mid + 1, right, node * 2 + 1, level - amount)


for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(take_candy(1, 10 ** 6, 1, query[1]))
    else:
        put_candy(1, 10 ** 6, 1, query[1], query[2])
