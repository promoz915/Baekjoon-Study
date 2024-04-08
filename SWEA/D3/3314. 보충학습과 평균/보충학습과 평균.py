T = int(input())

for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    for i in range(len(data)):
        if data[i] < 40:
            data[i] = 40
    ans = sum(data) // 5
    print(f'#{test_case} {ans}')