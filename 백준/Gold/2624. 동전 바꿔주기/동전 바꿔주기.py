import sys
input = sys.stdin.readline

t = int(input())
k = int(input())

dp = [0] * (t+1)
dp[0] = 1

data = []
for _ in range(k):
    p, n = map(int, input().split())
    data.append((p, n))
    
for coin, cnt in data:
    for money in range(t, 0, -1):
        for i in range(1, cnt + 1):
            if money - coin * i >= 0:
                dp[money] += dp[money - coin * i]
                
print(dp[t])