T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = arr[0]
    
    for i in range(n-1):
        if arr[i] >= 0 and (arr[i] + arr[i+1]) >= 0:
            arr[i+1] += arr[i]
        if max_val < arr[i+1]:
            max_val = arr[i+1]
    print(f'#{test_case} {max_val}')