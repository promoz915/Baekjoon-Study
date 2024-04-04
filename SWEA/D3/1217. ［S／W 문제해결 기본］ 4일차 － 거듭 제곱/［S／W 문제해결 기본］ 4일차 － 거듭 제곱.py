def func(a, b):
    if b == 0:
        return (1)
    else:
        return (func(a, b-1) * a)
    
for _ in range(1, 11):
    test_case = int(input())
    n, m = map(int, input().split())
    ans = func(n, m)
    print(f'#{test_case} {ans}')