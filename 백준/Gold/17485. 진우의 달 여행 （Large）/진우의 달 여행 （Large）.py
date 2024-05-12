import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = data[0][j]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (j == 0 and k == 2) or (j == m-1 and k == 0):
                dp[i][j][k] = 10**6
                continue
            if k == 0:
                dp[i][j][k] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + data[i][j]
            elif k == 1:
                dp[i][j][k] = min(dp[i-1][j][0], dp[i-1][j][2]) + data[i][j]
            else:
                dp[i][j][k] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + data[i][j]

ans = 1e9
for j in range(m):
    ans = min(ans, min(dp[n-1][j]), ans)
print(ans)