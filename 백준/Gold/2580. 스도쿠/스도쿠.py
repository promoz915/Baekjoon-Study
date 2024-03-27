import sys; input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
blank = []

def row(a, n):
    for i in range(9):
        if n == arr[a][i]:
            return False
    return True

def col(a, n):
    for i in range(9):
        if n == arr[i][a]:
            return False
    return True

def square(y, x, n):
    for i in range(3):
        for j in range(3):
            if n == arr[y//3 * 3 + i][x//3 * 3 + j]:
                return False
    return True

def find(n):
    if n == len(blank):
        for i in arr:
            print(*i)
        exit()

    for i in range(1, 10):
        y = blank[n][0]
        x = blank[n][1]
        if col(x, i) and row(y, i) and square(y, x, i):
            arr[y][x] = i
            find(n+1)
            arr[y][x] = 0

for i in range(9):
    for j in range(9):
         if arr[i][j] == 0:
             blank.append([i, j])

find(0)