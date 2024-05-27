import sys

input = sys.stdin.readline

for _ in range(int(input())):
    island = []
    n = int(input())
    for _ in range(n):
        island.append(list(map(int, input().split())))

    island.sort(key=lambda x: -x[1])
    temp = 0
    for i in range(n - 1):
        if island[i][1] != island[i + 1][1]:
            island[i][1] = temp
            temp += 1
        else:
            island[i][1] = temp
    island[n - 1][1] = temp
    island.sort(key=lambda x: x[0])

    tree = [0] * 2 * n
    result = 0
    for i in island:

        x, y = i
        left = n
        right = y + n + 1
        while left < right:
            if left % 2:
                result += tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += tree[right]
            left //= 2
            right //= 2

        y += n
        while y:
            tree[y] += 1
            if y % 2:
                y -= 1
            y //= 2
    print(result)
