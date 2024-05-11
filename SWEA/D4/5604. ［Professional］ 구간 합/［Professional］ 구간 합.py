def check(n, t):
    global ans
    while n > 0:
        ans += (n % 10) * t
        n //= 10
        
t = int(input())
for test_case in range(1, t+1):
    a, b = map(int, input().split())
    ans = 0
    mul = 1
    
    while a <= b:
        while a % 10 != 0 and a <= b:
            check(a, mul)
            a += 1
        if a > b or (a == 0 and b == 0):
            break
        while b % 10 != 9 and a <= b:
            check(b, mul)
            b -= 1
       
        a //= 10
        b //= 10
        
        m = (b - a + 1) * mul
        for i in range(10):
            ans += m * i
        mul *= 10
    
    print(f'#{test_case} {ans}')