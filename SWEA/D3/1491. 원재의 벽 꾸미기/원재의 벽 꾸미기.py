T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    val = -1
    for r in range(1, n+1):
        c = 1
        while r * c <= n:
            num = a * (abs(r-c)) + b * (n-r*c)
            if val == -1:
                val = num
            else:
                val = min(val, num)
            c += 1
    print(f'#{test_case} {val}')