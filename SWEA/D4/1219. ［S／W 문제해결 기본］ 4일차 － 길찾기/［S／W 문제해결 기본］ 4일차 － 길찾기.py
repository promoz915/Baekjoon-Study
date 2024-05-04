for _ in range(1, 11):
    test_case, n = map(int, input().split())
    data = list(map(int, input().split()))
    
    visited = [False] * 100
    road = [[] for _ in range(100)]
    for i in range(n):
        road[data[i*2]].append(data[i*2+1])
    
    stack = [0]
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            
            for i in road[now]:
                if not visited[i]:
                    stack.append(i)
                    
    if visited[99]:
        result = 1
    else:
        result = 0
        
        
    print(f'#{test_case} {result}')