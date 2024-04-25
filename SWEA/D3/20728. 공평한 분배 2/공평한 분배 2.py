answer = []
t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    s_data = sorted(data)
    ans = 1e9
    
    for i in range(n - k + 1):
        max_candy = s_data[i + k - 1]
        min_candy = s_data[i]
        temp = max_candy - min_candy
        ans = min(ans, temp)
        
    answer.append(f'#{test_case} {ans}')

for a in answer:
    print(a)