def dfs(b_idx, o_idx, time):
    while len(blue) != 0 or len(orange) != 0:
        if data[0] == 'B':
            if int(data[1]) - 1 > b_idx:
                b_idx += 1
            elif int(data[1]) - 1 < b_idx:
                b_idx -= 1
            else:
                data.pop(0)
                data.pop(0)
                blue.pop(0)
            
            if len(orange) != 0:
                if o_idx < orange[0] - 1:
                    o_idx += 1
                elif o_idx > orange[0] - 1:
                    o_idx -= 1
        else:
            if int(data[1]) - 1 > o_idx:
                o_idx += 1
            elif int(data[1]) - 1 < o_idx:
                o_idx -= 1
            else:
                data.pop(0)
                data.pop(0)
                orange.pop(0)
            
            if len(blue) != 0:
                if b_idx < blue[0] - 1:
                    b_idx += 1
                elif b_idx > blue[0] - 1:
                    b_idx -= 1
        time += 1
    return time

T = int(input())

for test_case in range(1, T + 1):
    data = list(map(str, input().split()))
    n = int(data.pop(0))
    
    blue = []
    orange = []
    
    for i in range(n):
        if data[2*i] == 'B':
            blue.append(int(data[2*i+1]))
        else:
            orange.append(int(data[2*i+1]))
            
    print(f'#{test_case} {dfs(0, 0, 0)}')