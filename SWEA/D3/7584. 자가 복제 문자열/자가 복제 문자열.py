T = int(input())

for test_case in range(1, T + 1):
    k = int(input())
    temp = 2
    cnt = 0
    while k > 2:
        temp = 2
        while temp < k:
            temp *= 2
        if temp == k:
            break
        k = temp - k
        cnt += 1
    ans = cnt % 2
    print(f'#{test_case} {ans}')
