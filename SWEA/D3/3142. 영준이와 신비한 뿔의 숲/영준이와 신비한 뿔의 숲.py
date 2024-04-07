t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    y = n-m
    x = m-y
    print(f'#{test_case} {x} {y}')