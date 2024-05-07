t = int(input())
for test_case in range(1, t+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    
    ans = [0]
    for i in range(n):
        for j in range(len(ans)):
            ans.append(h[i] + ans[j])
    
    ans = list(set(ans))
    
    temp = []
    for a in ans:
        if a - b >= 0:
            temp.append(a - b)
    result = min(temp)
    
    print(f'#{test_case} {result}')