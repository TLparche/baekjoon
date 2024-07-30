import sys

input = sys.stdin.readline


def heap_push(val):
    heap.append(val)
    index = len(heap) - 1
    while index != 1:
        temp = index // 2
        if heap[temp] > heap[index]:
            break
        heap[index], heap[temp] = heap[temp], heap[index]
        index = temp


def heap_pop():
    heap[1], heap[-1] = heap[-1], heap[1]
    top_val = heap.pop()
    size = len(heap) - 1
    index = 1
    while 2 * index <= size:
        left = 2 * index
        right = 2 * index + 1
        if right <= size and heap[left] < heap[right]:
            temp = right
        else:
            temp = left

        if heap[index] < heap[temp]:
            heap[index], heap[temp] = heap[temp], heap[index]
            index = temp
        else:
            break
    return top_val


n = int(input())
heap = [0]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

zipped_pairs = sorted(zip(b, a))
b_sorted, a_sorted = zip(*zipped_pairs)

result = a_sorted[0]
for i in range(1, n - 1, 2):
    heap_push(a_sorted[i])
    heap_push(a_sorted[i + 1])
    result += heap_pop()
print(result)
