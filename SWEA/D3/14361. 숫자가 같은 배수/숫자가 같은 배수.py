T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = input()
    n_list = sorted(list(n))
    
    flag = False
    k = 2
    while True:
        n_mul = int(n) * k
        if len(str(n_mul)) > len(n):
            break
        if sorted(list(str(n_mul))) == n_list:
            flag = True
            break
        k += 1
        
    if flag:
        ans = 'possible'
    else:
        ans = 'impossible'
    print(f'#{test_case} {ans}')