from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

def up(arr):
    for j in range(n):
        direct = 0
        for i in range(1, n):
            if arr[i][j] != 0:
                temp = arr[i][j]
                arr[i][j] = 0

                if arr[direct][j] == 0:
                    arr[direct][j] = temp

                elif arr[direct][j] == temp:
                    arr[direct][j] *= 2
                    direct += 1

                else:
                    direct += 1
                    arr[direct][j] = temp
    return arr

def down(arr):
    for j in range(n):
        direct = n-1
        for i in range(n-2, -1, -1):
            if arr[i][j] != 0:
                temp = arr[i][j]
                arr[i][j] = 0

                if arr[direct][j] == 0:
                    arr[direct][j] = temp

                elif arr[direct][j] == temp:
                    arr[direct][j] *= 2
                    direct -= 1

                else:
                    direct -= 1
                    arr[direct][j] = temp
    return arr

def left(arr):
    for i in range(n):
        direct = 0
        for j in range(1, n):
            if arr[i][j] != 0:
                temp = arr[i][j]
                arr[i][j] = 0

                if arr[i][direct] == 0:
                    arr[i][direct] = temp

                elif arr[i][direct] == temp:
                    arr[i][direct] *= 2
                    direct += 1

                else:
                    direct += 1
                    arr[i][direct] = temp
    return arr

def right(arr):
    for i in range(n):
        direct = n-1
        for j in range(n-2, -1, -1):
            if arr[i][j] != 0:
                temp = arr[i][j]
                arr[i][j] = 0

                if arr[i][direct] == 0:
                    arr[i][direct] = temp

                elif arr[i][direct] == temp:
                    arr[i][direct] *= 2
                    direct -= 1

                else:
                    direct -= 1
                    arr[i][direct] = temp
    return arr

def dfs(cnt, arr):
    if cnt == 5:
        return max(map(max, arr))

    return max(dfs(cnt + 1, up(deepcopy(arr))), dfs(cnt + 1, down(deepcopy(arr))),
               dfs(cnt + 1, left(deepcopy(arr))), dfs(cnt + 1, right(deepcopy(arr))))

print(dfs(0, data))