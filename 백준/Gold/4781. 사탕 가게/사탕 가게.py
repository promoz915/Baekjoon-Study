import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n = int(n)

    if n == 0 and m == 0.00:
        break

    m = int(m * 100 + 0.5)

    dp = [0 for _ in range(m+1)]
    for _ in range(n):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)

        for i in range(p, m+1):
            dp[i] = max(dp[i-p] + c, dp[i])
    print(dp[m])