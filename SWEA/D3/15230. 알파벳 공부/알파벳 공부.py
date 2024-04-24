check_list = 'abcdefghijklmnopqrstuvwxyz'

t = int(input())
ans = []
for test_case in range(1, t+1):
    data = input()
    cnt = 0

    for i in range(len(data)):
        if data[i] == check_list[i]:
            cnt += 1
        else:
            break

    ans.append(f'#{test_case} {cnt}')

for a in ans:
    print(a)