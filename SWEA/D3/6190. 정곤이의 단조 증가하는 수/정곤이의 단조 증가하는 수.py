def check(a):
    a = str(a)
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            num = data[i] * data[j]
            if check(num):
                ans = max(ans, num)
        if ans == 0:
            ans = -1

    print(f'#{test_case} {ans}')