T = int(input())
day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m, d = map(int, input().split())
    date = 0
    for i in range(m):
        date += day[i]
    date += d
    date %= 7
    ans = (date + 3) % 7
    print(f'#{test_case} {ans}')
