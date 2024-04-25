t = int(input())
ans = []
for test_case in range(1, t+1):
    data = list(map(int, input().split()))
    eat = 0

    if data[1] < 2 or data[2] < 3:
        print(f'#{test_case} -1')
        continue

    if data[2] - data[1] < 1:
        eat += data[1] - data[2] + 1
        data[1] = data[2] - 1

    if data[1] - data[0] < 1:
        eat += data[0] - data[1] + 1

    ans.append(f'#{test_case} {eat}')

for a in ans:
    print(a)