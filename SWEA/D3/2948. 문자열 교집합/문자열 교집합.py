t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    num = n + m
    list_n = list(input().split())
    list_m = list(input().split())
    list_merge = list_n + list_m
    ans = num - len(set(list_merge))
    
    print(f'#{test_case} {ans}')