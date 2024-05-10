t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    temp = n * m
    
    cnt1 = 0
    for w in range(n-2):
        for k in range(m):
            if board[w][k] != 'W':
                cnt1 += 1
        
        cnt2 = 0
        for b in range(w+1, n-1):
            for k in range(m):
                if board[b][k] != 'B':
                    cnt2 += 1
            
            cnt3 = 0
            for r in range(b+1, n):
                for k in range(m):
                    if board[r][k] != 'R':
                        cnt3 += 1
                        
            cnt = cnt1 + cnt2 + cnt3
            if temp > cnt:
                temp = cnt
     
    print(f'#{test_case} {temp}')
            