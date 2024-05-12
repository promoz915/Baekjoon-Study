t = int(input())
for test_case in range(1, t+1):
    a, b = input().split()
    ans = len(a) - (len(b)-1) * a.count(b)
    print(f'#{test_case} {ans}')