T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ans = 0
    for _ in range(n):
        p, x = map(float, input().split())
        ans += p * x
    print(f'#{test_case} {ans}')