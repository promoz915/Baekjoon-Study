dct = {}
r_dct = {}

i, j = 1, 1

for n in range(1, 50000):
    dct[n] = (i,j)
    r_dct[(i,j)] = n
    i, j = i+1, j-1
    if j < 1:
        i, j = 1, i

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    
    pi, pj = dct[p]
    qi, qj = dct[q]
    
    ans = r_dct[(pi+qi, pj+qj)]
    print(f'#{test_case} {ans}')