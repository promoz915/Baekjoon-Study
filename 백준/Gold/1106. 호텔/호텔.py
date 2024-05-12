import sys
input = sys.stdin.readline

c, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [1e9 for _ in range(c+100)]
dp[0] = 0

for cost, num in data:
    for i in range(num, c+100):
        dp[i] = min(dp[i-num]+cost, dp[i])

print(min(dp[c:]))