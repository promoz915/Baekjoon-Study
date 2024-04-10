from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    data = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        data[a].append(b)
        data[b].append(a)
    
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i in data[j] and j in data[k] and k in data[i]:
                    ans +=1 
                    
    print(f'#{test_case} {ans}')