T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = round(pow(n, 1/3))

    if data ** 3 == n:
        print(f'#{test_case} {data}')
    else:
        print(f'#{test_case} {-1}')