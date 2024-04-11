t = int(input())
for test_case in range(1, t + 1):
    n, a, b = map(int, input().split())
    max_ = min(a, b)
    min_ = a + b - n
    if min_ < 0 : min_ = 0
    print(f'#{test_case} {max_} {min_}')