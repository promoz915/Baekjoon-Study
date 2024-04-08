T = int(input())

for test_case in range(1, T + 1):
    l, u, x = map(int, input().split())
    ans = 0
    if x < l:
        ans = l-x
    elif x > u:
        ans = -1
    print(f'#{test_case} {ans}')
