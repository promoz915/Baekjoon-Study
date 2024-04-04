T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ori = list(map(int, input().split()))
    o = int(input())
    change = list(input().split())

    temp = ''
    a = -1
    b = -1
    for i in range(len(change)):
        if change[i] in ['I', 'D', 'A']:
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

                    ori.insert(a, change[i])
                    a += 1

            elif temp == 'D':
                if a == -1:
                    a = int(change[i])
                    continue
                else:
                    if b == -1:
                        b = int(change[i])
                        for j in range(b):
                            del ori[a]
            elif temp == 'A':
                if b == -1:
                    b = int(change[i])
                else:
                    ori.append(int(change[i]))
    print(f'#{test_case}', *ori[:10])