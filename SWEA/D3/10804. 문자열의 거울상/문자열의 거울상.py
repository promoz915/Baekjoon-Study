T = int(input())

for test_case in range(1, T + 1):
    data = input()
    ans = ''

    for i in range(len(data)-1, -1, -1):
        if data[i] == 'b':
            ans += 'd'
        elif data[i] == 'd':
            ans += 'b'
        elif data[i] == 'p':
            ans += 'q'
        else:
            ans += 'p'

    print(f'#{test_case} {ans}')