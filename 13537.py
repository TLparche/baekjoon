import sys
from bisect import bisect_right

input = sys.stdin.readline


def merge_sort(graph, index):
    if len(graph) <= 1:
        seg_tree[index] = graph
        return graph
    mid = (len(graph) + 1) // 2
    left = merge_sort(graph[:mid], index * 2)
    right = merge_sort(graph[mid:], index * 2 + 1)

    merge_arr = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1
    merge_arr += left[l:]
    merge_arr += right[r:]
    seg_tree[index] = merge_arr
    return merge_arr


def query(curNode, left, right, start, end, tar):
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return len(seg_tree[curNode]) - bisect_right(seg_tree[curNode], tar)

    leftNode = 2 * curNode
    rightNode = leftNode + 1
    mid = (left + right) // 2

    return (query(leftNode, left, mid, start, end, tar) +
            query(rightNode, mid + 1, right, start, end, tar))


n = int(input())
arr_num = list(map(int, input().split()))
m = int(input())
seg_tree = [[0] for _ in range(n * 4 + 1)]
merge_sort(arr_num, 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    print(query(1, 1, n, i, j, k))
