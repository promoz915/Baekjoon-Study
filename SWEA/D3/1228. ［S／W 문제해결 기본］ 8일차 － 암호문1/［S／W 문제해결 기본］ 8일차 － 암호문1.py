T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    orig = list(map(int, input().split()))
    o = int(input())
    change = list(input().split())
    
    temp = ''
    a = -1
    b = -1
    
    for i in range(len(change)):
        if change[i] == 'I':
            temp = change[i]
            a = -1
            b = -1
        else:
            if temp == 'I':
                if a == -1:
                    a = int(change[i])
                    continue
                else:
                    if b == -1:
                        b = int(change[i])
                        continue
                    orig.insert(a, change[i])
                    a += 1
    print(f'#{test_case}', *orig[:10])