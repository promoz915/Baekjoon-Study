def func(idx, num):
    global ans
    
    if idx == n:
        ans = max(ans, num)
        return
    
    if num <= ans:
        return
    
    for i in range(n):
        if visited[i]:
            continue
       
        if data[idx][i] == 0:
            continue
        
        visited[i] = 1
        func(idx+1, num*(data[idx][i]/100))
        visited[i] = 0


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = -1
    func(0, 100)
    
    print(f'#{test_case}', '{:.6f}'.format(round(ans, 6)))
    