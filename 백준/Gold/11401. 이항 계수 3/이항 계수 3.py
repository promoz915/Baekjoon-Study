MOD = 1000000007

n, k = map(int, input().split())

# a의 b 거듭제곱 구하기
def func(a, b):
    ab = 1
    while b > 0:
        if b % 2 == 1:
            ab *= a
            b -= 1
            ab %= MOD
        a *= a
        a %= MOD
        b /= 2
    return ab
# r1 : 분자(n!), r2 : 분모(n-k)! * k!
r1, r2 = 1, 1

for i in range(1, n+1):
    r1 *= i
    r1 %= MOD

for i in range(1, k+1):
    r2 *= i
    r2 %= MOD

for i in range(1, n-k+1):
    r2 *= i
    r2 %= MOD

r2 = func(r2, MOD-2)
r2 %= MOD
r1 *= r2
r1 %= MOD
print(r1)