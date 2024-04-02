T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    temp += arr[x][y]
            ans = max(ans, temp)
    print(f'#{test_case} {ans}')