T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    
    temp = 0
    idx = 0
    flag = True
    
    for i in range(0, people[-1]+1):
        if i > 0 and i % m == 0:
            temp += k
        if people[idx] <= i:
            if temp > 0:
                temp -= 1
                idx += 1
            else:
                flag = False
                break
    if flag:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')