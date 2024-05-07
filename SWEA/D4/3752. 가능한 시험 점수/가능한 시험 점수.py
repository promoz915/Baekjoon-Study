t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))
    ans = [0]
    
    for d in data:
        ans = list(set(ans))
        for i in range(len(ans)):
            ans.append(ans[i] + d)
            
    print(f'#{test_case} {len(set(ans))}')
        