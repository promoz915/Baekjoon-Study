from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    dict = defaultdict(int)
    flag = True
    
    for i in data:
        dict[i] += 1
        
    if len(dict) != 2:
        flag = False
    
    else:
        flag = True
        for val in dict.values():
            if val != 2:
                flag = False
                break
    
    if flag:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')