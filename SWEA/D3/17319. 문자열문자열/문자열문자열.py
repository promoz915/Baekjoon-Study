t = int(input())
ans = []
for test_case in range(1, t+1):
    n = int(input())
    s = input()
    flag = True
    if len(s) % 2 != 0:
        flag = False
    else:
        if s[:len(s)//2] == s[len(s)//2:]:
            flag = True
        else:
            flag = False
    if flag:
        ans.append(f'#{test_case} Yes')
    else:
        ans.append(f'#{test_case} No')

for a in ans:
    print(a)