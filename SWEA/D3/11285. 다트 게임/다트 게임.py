import math

ans = []
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    total = 0
    for _ in range(n):
        x, y = map(int, input().split())
        r = math.ceil(math.sqrt(x*x+y*y)/20)
        
        if r <= 0:
            total += 10
        elif r <= 10:
            total += 11-r
    ans.append(f'#{test_case} {total}')
    
for a in ans:
    print(a)