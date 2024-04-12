T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, pd, pg = map(int, input().split())
    if pd != 0 and pg == 0:
        flag = False
    elif pd != 100 and pg == 100:
        flag = False
    else:
        flag = False
        for i in range(1, n+1):
            if (i * pd) / 100 == (i * pd) // 100:
                flag = True
                break
    if flag:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Broken')
