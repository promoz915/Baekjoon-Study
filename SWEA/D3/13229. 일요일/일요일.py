week = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 7}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    if data == 'SUN':
        print(f'#{test_case} 7')
    else:
        print(f'#{test_case} {week["SUN"] - week[data]}')