T = int(input())
ans = ''
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())

    if a and not b and not c and not d:
        ans = '0' * (a+1)
    elif d and not a and not b and not c:
        ans = '1' * (d+1)
    elif b == c and b:
        ans = '0' * (a+1) + '10' * (b-1) + '1' * (d+1) + '0'
    elif b - c == 1:
        ans = '0' * (a+1) + '10' * c + '1' * (d+1)
    elif c - b == 1:
        ans = '1' * (d+1) + '01' * b + '0' * (a+1)
    else:
        ans = 'impossible'
        
    print(f'#{test_case} {ans}')