import sys; input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for j in range(1001)] for i in range(1001)]
size = 0

for i in range(n):
    num = list(input())
    for j in range(m):
        arr[i][j] = int(num[j])
        if arr[i][j] == 1 and j > 0 and i > 0:
            arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + arr[i][j]
        if size < arr[i][j]:
            size = arr[i][j]

print(size**2)