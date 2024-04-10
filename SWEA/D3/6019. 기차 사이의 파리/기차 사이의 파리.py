T = int(input())
for test_case in range(1, T + 1):
    d, a, b, f = map(int, input().split())
    ans = (d/(a+b)) * f
    print(f'#{test_case} {ans}')