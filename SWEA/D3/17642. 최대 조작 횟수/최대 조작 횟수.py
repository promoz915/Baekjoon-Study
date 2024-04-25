t = int(input())
ans = []
for test_case in range(1, t+1):
    a, b = map(int, input().split())

    if b - a == 0:
        result = 0

    elif a > b or b - a == 1:
        result = -1

    else:
        result = (b-a) // 2

    ans.append(f'#{test_case} {result}')


for a in ans:
    print(a)