MOD = 1234567891

def func(N):
    n = 1
    for i in range(2, N+1):
        n = (n*i) % MOD
    return n

def nemo(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = nemo(n, k//2)
    
    if k % 2 == 0:
        return tmp * tmp % MOD
    else:
        return tmp * tmp * n % MOD

t = int(input())

for test_case in range(1, t+1):
    
    N, K = map(int, input().split())
    num1 = func(N)
    num2 = func(N-K) * func(K) % MOD
    ans = num1 * nemo(num2, MOD-2) % MOD

    print(f'#{test_case} {ans}')