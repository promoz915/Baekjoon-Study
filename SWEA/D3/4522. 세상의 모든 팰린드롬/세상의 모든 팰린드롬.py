T = int(input())

for test_case in range(1, T + 1):
    data = input()
    data_len = len(data)
    ans = 'Exist'
    for i in range(data_len // 2):
        if data[i] != data[data_len-i-1] and data[i] != '?' and data[data_len-i-1] != '?':
            ans = 'Not exist'
            break
    print(f'#{test_case} {ans}')