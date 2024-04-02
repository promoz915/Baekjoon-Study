import sys;input = sys.stdin.readline

MOD = 1000000007
n, l, r = map(int, input().split())
arr = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]
arr[1][1][1] = 1

for i in range(2, n+1):
    for j in range(1, l+1):
        for k in range(1, r+1):
            arr[i][j][k] = ((arr[i-1][j-1][k]) + (arr[i-1][j][k-1]) + (arr[i-1][j][k] * (i-2))) % MOD

print(arr[n][l][r])