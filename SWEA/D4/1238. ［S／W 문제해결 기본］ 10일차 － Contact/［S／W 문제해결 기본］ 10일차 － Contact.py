for test_case in range(1, 11):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))
    c = [[0] * 101 for _ in range(101)]
    for i in range(0, length, 2):
        c[data[i]][data[i+1]] = 1
    
    check = [0] * 101
    check[start] = 1
    
    queue = [start]
    result = start
    
    while queue:
        n = queue.pop(0)
        
        if check[result] < check[n] or (check[result] == check[n] and result < n):
            result = n
        
        for i in range(101):
            if c[n][i] and check[i] == 0:
                queue.append(i)
                check[i] = check[n] + 1
                
    print(f'#{test_case} {result}')