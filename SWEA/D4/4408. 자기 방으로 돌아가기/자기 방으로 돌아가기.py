t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    a = [0] * 200
    
    for _ in range(n):
        s, e = map(int, input().split())
        s = (s-1) // 2
        e = (e-1) // 2
        
        for i in range(min(s,e), max(s,e)+1):
            a[i] += 1
    
    print(f'#{test_case} {max(a)}')