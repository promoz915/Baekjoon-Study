T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt = 1
            if arr[j][i] == 2 and cnt:
                ans += 1
                cnt = 0
    print(f'#{test_case} {ans}')