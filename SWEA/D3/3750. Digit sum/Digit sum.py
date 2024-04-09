T = int(input())
a = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = list(input()) 
    while len(n) != 1:
        temp = 0
        for i in range(len(n)):
            temp += int(n[i])
        n = str(temp)
    a.append(n[0])
for test_case in range(1, T + 1):
    print(f'#{test_case} {a[test_case-1]}')