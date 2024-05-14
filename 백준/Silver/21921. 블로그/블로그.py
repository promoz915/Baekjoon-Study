import sys
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

if max(data) == 0:
    print('SAD')
else:
    temp = sum(data[:x])
    cnt = 1
    max_temp = temp
    
    for i in range(x, n):
        temp += data[i]
        temp -= data[i-x]
        
        if max_temp < temp:
            max_temp = temp
            cnt = 1
        elif max_temp == temp:
            cnt += 1
    
    print(max_temp)
    print(cnt)