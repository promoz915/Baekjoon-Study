T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ans = [0] * 5
    num = [2, 3, 5, 7, 11]
    
    for i in range(4, -1, -1):
        while n % num[i] == 0:
            ans[i] += 1
            n //= num[i]
    print(f'#{test_case}', end=' ')
    print(*ans)