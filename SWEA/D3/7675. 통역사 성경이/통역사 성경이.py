check = ['.', '!', '?']
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0
    i = 0
    ans = []

    while i < n:
        data = list(input().split())
        for name in data:
            name_strip = name.rstrip('.?!')
            
            if (len(name_strip) == 1 and name_strip.isupper()) or (
                    name_strip[0].isupper() and name_strip.isalpha() and name_strip[1:].islower()):
                cnt += 1
                
            if name[-1] in check:
                ans.append(cnt)
                cnt = 0
                i += 1
    print(f'#{test_case}', *ans)