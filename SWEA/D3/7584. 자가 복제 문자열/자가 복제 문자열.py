t = int(input())
for test_case in range(1, t+1):
    k = int(input()) - 1
    ans = 0
    while k > 0:
        if k % 2 == 1:
            k = (k-1)//2
        if k % 4 == 0:
            ans = 0
            break
        elif k % 2 == 0:
            ans = 1
            break
    print(f'#{test_case} {ans}')
