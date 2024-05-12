t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    names = [input() for _ in range(n)]
    names = list(set(names))
    re_names = sorted(names, key=lambda x: (len(x), x))
    
    print(f'#{test_case}')
    for r in re_names:
        print(r)