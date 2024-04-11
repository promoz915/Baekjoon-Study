from collections import defaultdict

T = int(input())

for test_case in range(1, T + 1):
    data = input()
    dd = defaultdict(int)
    ans = ''
    
    for d in data:
        dd[d] += 1
    
    for key in dd.keys():
        dd[key] %= 2
     
    for key, value in dd.items():
        if value > 0:
            ans += key
    
    if ans:
        ans = sorted(ans)
        print(f'#{test_case} {"".join(ans)}')
    else:
        print(f'#{test_case} Good')
            
    
            