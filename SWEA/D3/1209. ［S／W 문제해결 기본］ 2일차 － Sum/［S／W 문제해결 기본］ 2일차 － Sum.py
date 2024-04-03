for _ in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    
    for i in range(100):
        a = 0
        for j in range(100):
            a += arr[i][j]
            ans = max(ans, a)
    for i in range(100):
        a = 0
        for j in range(100):
            a += arr[j][i]
            ans = max(ans, a)
    a = 0
    for i in range(100):
        a += arr[i][i]
        ans = max(ans, a)
    print(f'#{test_case} {ans}')