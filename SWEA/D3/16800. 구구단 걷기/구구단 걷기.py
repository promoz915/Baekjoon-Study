import math

t = int(input())
ans = []
for test_case in range(1, t+1):
    n = int(input())
    x, y = 0, 0
    
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0:
            x, y = i, n//i
            break
    temp = x + y - 2
    ans.append(f'#{test_case} {temp}')
    
for a in ans:
    print(a)