t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))
    sum_ = sum(data)
    avg_ = sum_ / n
    ans = 0
    for i in data:
        if i <= avg_:
            ans += 1
    print(f'#{test_case} {ans}')