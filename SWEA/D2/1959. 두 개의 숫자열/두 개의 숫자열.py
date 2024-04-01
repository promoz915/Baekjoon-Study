T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    
    for i in range(abs(n-m)+1):
        temp = 0
        for j in range(min(n,m)):
            if n < m:
                temp += a[j] * b[j+i]
            else:
                temp += a[j+i] * b[j]
        ans = max(ans, temp)
    print(f"#{test_case} {ans}")