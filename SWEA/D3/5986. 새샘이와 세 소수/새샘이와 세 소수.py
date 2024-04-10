prime = []
for i in range(2, 1000):
    for j in range(2, i//2+1):
        if i % j == 0:
            break
    else:
        prime.append(i)
        
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ans = 0
    for i in range(len(prime)):
        if n > prime[i]:
            for j in range(i, len(prime)):
                if n > prime[j]:
                    for k in range(j, len(prime)):
                        if prime[i] + prime[j] + prime[k] == n:
                            ans += 1
    print(f'#{test_case} {ans}')