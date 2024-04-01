import sys; input = sys.stdin.readline

n = int(input())
d = [[0 for j in range(11)] for i in range(n+1)]
MOD = 1000000000

for i in range(1, 10):      # 길이가 1일 때 만드는 높이 h로 끝나는 계단 수의 모든 경우의 수는 1
    d[1][i] = 1

for i in range(2, n+1):
    d[i][0] = d[i-1][1]     # n에서 높이가 0이면 n-1에서는 높이가 1이어야 게단 수가 가능
    d[i][9] = d[i-1][8]     # n에서 높이가 9이면 n-1에서는 높이가 8이어야 계단 수가 가능
    for j in range(1, 9):
        d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % MOD

ans = 0
for i in range(10):
    ans = (ans + d[n][i]) % MOD
print(ans)