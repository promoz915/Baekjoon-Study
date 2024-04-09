T = int(input())
temp = []
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    num_a = a/b
    num_b = c/d
    if num_a > num_b: temp.append('ALICE')
    elif num_a < num_b: temp.append('BOB')
    else: temp.append('DRAW')

for test_case in range(1, T + 1):
    print(f'#{test_case} {temp[test_case-1]}')