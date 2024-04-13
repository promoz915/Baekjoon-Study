T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    val = 15 - len(data)
    if val < 0:
        val = 0
    
    if data.count('o') + val >= 8:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')