T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    
    max_num = -1e9
    sum_num = 0
    
    for i in range(n):
        sum_num += data[i]
        
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < 0:
            sum_num = 0
    print(f'#{test_case} {max_num}')