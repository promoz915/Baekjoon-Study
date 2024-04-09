def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a//gcd(a, b)*b

def func(m, n, x, y):
    max_year = lcm(m, n)
    k = x
    while k <= max_year:
        if (k-x) % m == 0 and (k-y) % n == 0:
            return k
        k += m
    return -1

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(func(m, n, x, y))