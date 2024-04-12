prime = [2]
for i in range(3, int(10000000**(0.5)), 2):
    for p in prime:
        if not i % p:
            break
    else:
        prime.append(i)
        
answer = []

t = int(input())
for test_case in range(1, t+1):
    a = int(input())
    ans = 1
    if a**0.5 != int(a**0.5):
        for p in prime:
            cnt = 0
            while not a % p:
                a //= p
                cnt += 1
            if cnt % 2:
                ans *= p
            if a == 1 or a < p:
                break
        if a > 1:
            ans *= a
    answer.append(f'#{test_case} {ans}')
    
for ans in answer:
    print(ans)