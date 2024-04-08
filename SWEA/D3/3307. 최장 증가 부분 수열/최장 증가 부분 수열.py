T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1
    
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1
        
    print(f'#{test_case} {max(dp)}')