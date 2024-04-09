T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    rev_data = data[::-1]
    ans = 'Not exist'
    data_len = len(data)
    for i in range(data_len//2):
        if data[i] == rev_data[i]:
            continue
        if data[i] == '*' or rev_data[i] == '*':
            ans = 'Exist'
            break
        else:
            break
    else:
        ans = 'Exist'
    print(f'#{test_case} {ans}')