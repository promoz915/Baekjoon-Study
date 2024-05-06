for _ in range(1, 11):
    test_case = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    
    min_val = 1e9
    ans = 0
    
    for i in range(100):
        if data[0][i] == 1:
            x, y = 0, i
            cnt = 0
            
            while x != 99:
                x += 1
                cnt += 1
                
                if y > 0 and data[x][y-1] == 1:
                    while y > 0 and data[x][y-1] == 1:
                        y -= 1
                        cnt += 1
                elif y < 99 and data[x][y+1] == 1:
                    while y < 99 and data[x][y+1] == 1:
                        y += 1
                        cnt += 1
            
            
            if min_val > cnt:
                min_val = cnt
                ans = i
      
    print(f'#{test_case} {ans}')