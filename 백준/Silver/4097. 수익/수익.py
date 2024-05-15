import sys
input = sys.stdin.readline

ans = []

while True:
    n = int(input())
    if n == 0:
        break

    data = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(n)]
    dp[0] = data[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1] + data[i], data[i])

    ans.append(max(dp))

for a in ans:
    print(a)