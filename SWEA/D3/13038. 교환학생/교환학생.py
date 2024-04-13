T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    ans = 1e9
    
    for i in range(7):
        if data[i] == 1:
            idx = i
            temp = n
            day = 0
            
            while temp:
                if data[idx] == 1:
                    temp -= 1
                day += 1
                idx = (idx+1) % 7
            
            if ans > day:
                ans = day
    print(f'#{test_case} {ans}')
                    