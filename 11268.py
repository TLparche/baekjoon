import sys


def swap(a, b):
    return b, a


n = int(sys.stdin.readline().strip())
heap = [0]
for i in range(n):
    x = int(sys.stdin.readline().strip())

    if x == 0:
        size = len(heap) - 1
        if size == 0:
            print(0)
        else:
            heap[1], heap[-1] = swap(heap[1], heap[-1])
            print(heap.pop())
            size -= 1
            index = 1
            while 2 * index <= size:
                left = 2 * index
                right = 2 * index + 1
                if right <= size and heap[left] > heap[right]:
                    temp = right
                else:
                    temp = left
                if heap[index] > heap[temp]:
                    heap[index], heap[temp] = swap(heap[index], heap[temp])
                    index = temp
                else:
                    break
    else:
        heap.append(x)
        index = len(heap) - 1
        while index != 1:
            temp = index // 2
            if abs(heap[temp]) < abs(heap[index]):
                break
            elif abs(heap[temp]) == abs(heap[index]):

            heap[index], heap[temp] = swap(heap[index], heap[temp])
            index = temp
