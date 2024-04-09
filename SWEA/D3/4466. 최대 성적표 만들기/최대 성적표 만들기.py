T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort(reverse=True)

    data_sum = 0
    for _ in range(k):
        data_sum += data.pop(0)
    print(f'#{test_case} {data_sum}')