import sys


def dfs(index):
    if index == len(loca):
        for i in range(9):
            print(*sudoku[i])
        exit()
    numb = set([i for i in range(1, 10)])
    x, y = loca[index]
    set1 = set(sudoku[x])
    set2 = set(transpose_sudoku[y])
    set3 = set()
    for i in range(3):
        for j in range(3):
            set3.add(sudoku[x - x % 3 + i][y - y % 3 + j])
    numb_list = list(numb - (set1 | set2 | set3))

    if len(numb_list) != 0:
        for i in numb_list:
            sudoku[x][y] = i
            transpose_sudoku[y][x] = i
            dfs(index + 1)
            sudoku[x][y] = 0
            transpose_sudoku[y][x] = 0
    return


sudoku = [[] * 9] * 9
for i in range(9):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    sudoku[i] = temp

loca = []
transpose_sudoku = [[0 for i in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            loca.append([i, j])
        transpose_sudoku[i][j] = sudoku[j][i]
dfs(0)
