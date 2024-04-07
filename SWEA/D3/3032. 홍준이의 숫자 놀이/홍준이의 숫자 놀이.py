def gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd(b, a%b)
        return d, y, x-y*(a//b)

def func(n,m):
    d, x, y = gcd(n, m)
    if d != 1:
        return (-1)
    else:
        return x, y
t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    p, q = func(n, m)
    print(f'#{test_case} {p} {q}')