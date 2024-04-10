T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if data[i-1][1] <= j:
                dp[i][j] = max(dp[i-1][j-data[i-1][1]] + data[i-1][0], dp[i-1][j]) 
            else:
                dp[i][j] = dp[i-1][j]
    print(f'#{test_case} {dp[n][k]}')