T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[1 for j in range(i)] for i in range(1, n+1)]
    
    for i in range(2, n):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{test_case}')
    for i in arr:
        print(*i)