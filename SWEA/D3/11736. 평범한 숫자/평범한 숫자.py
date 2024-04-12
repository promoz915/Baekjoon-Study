T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    
    for i in range(1, n-1):
        left, right = data[i-1], data[i+1]
        if data[i] != min(left, right, data[i]) and data[i] != max(left, right, data[i]):
            cnt += 1
    print(f'#{test_case} {cnt}')