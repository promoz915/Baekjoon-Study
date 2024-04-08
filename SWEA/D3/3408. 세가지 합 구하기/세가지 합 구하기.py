T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    s1 = ((1+n)*n)//2
    s2 = n**2
    s3 = n*(n+1)
    print(f'#{test_case} {s1} {s2} {s3}')