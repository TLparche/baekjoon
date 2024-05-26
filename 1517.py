import sys

input = sys.stdin.readline


def merge_sort(graph):
    if len(graph) <= 1:
        return graph, 0
    mid = len(graph) // 2
    left, left_inv = merge_sort(graph[:mid])
    right, right_inv = merge_sort(graph[mid:])

    merge_arr = []
    l, r = 0, 0
    inv = left_inv + right_inv
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            inv += len(left) - l
            r += 1
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr, inv


n = int(input())
arr_num = list(map(int, input().split()))
print(merge_sort(arr_num)[1])
