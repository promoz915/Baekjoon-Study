T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = list(input().split())
    if len(data) % 2 == 0:
        a = data[:len(data)//2]
        b = data[len(data)//2:]
    else:
        a = data[:len(data)//2+1]
        b = data[len(data)//2+1:]
    
    ans = []
    while a or b:
        if a:
            ans.append(a.pop(0))
        if b:
            ans.append(b.pop(0))
    print(f'#{test_case}', *ans)