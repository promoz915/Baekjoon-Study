T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ans = ''
    
    for _ in range(n):
        a, b = input().split()
        ans += a * int(b)
        
    print(f'#{test_case}')
    for i in range(0, len(ans), 10):
        print(ans[i:i+10])