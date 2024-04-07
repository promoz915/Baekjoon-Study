T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    s, e = n//2, n//2
    ans = 0
    
    for i in range(n):
        for j in range(s, e+1):
            ans += a[i][j]
        
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{test_case} {ans}')