T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    count = [13] * 4
    a = []
    for i in range(0, len(data), 3):
        if data[i] == 'S':
            count[0] -= 1
        elif data[i] == 'D':
            count[1] -= 1
        elif data[i] == 'H':
            count[2] -= 1
        else:
            count[3] -= 1
        if data[i:i+3] in a:
            count = ('ERROR')
            break
        a.append(data[i:i+3])
    if count == 'ERROR':
        print(f'#{test_case} {count}')
    else:
        print(f'#{test_case}', *count)