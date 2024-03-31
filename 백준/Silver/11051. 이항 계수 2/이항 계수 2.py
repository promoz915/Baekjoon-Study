import sys; input = sys.stdin.readline

n, k = map(int,input().split())
d = [[0 for j in range(n+1)] for i in range(n+1)]
MOD = 10007

for i in range(n+1):
    d[i][0] = 1
    d[i][i] = 1
    d[i][1] = i

for i in range(2, n+1):
    for j in range(1, i):
        d[i][j] = d[i-1][j] + d[i-1][j-1]
        d[i][j] = d[i][j] % MOD

print(d[n][k])