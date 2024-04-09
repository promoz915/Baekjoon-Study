t = int(input())
for test_case in range(1, t+1):
    data = input()
    n = int(input())
    bar = list(map(int, input().split()))
    bar.sort()
    ans = ''
    
    for i in range(len(data)):
        if bar:
            while bar[0] == i:
                ans += '-'
                bar.pop(0)
                if len(bar) == 0:
                    break
        ans += data[i]
        
    if bar:
        ans += '-' * len(bar)
    
    print(f'#{test_case} {ans}')