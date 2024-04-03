T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(int(input()) for _ in range(n))
    avg_val = sum(arr) // n
    
    ans = 0
    for i in arr:
        if i > avg_val:
            ans += i - avg_val
    print(f'#{test_case} {ans}')