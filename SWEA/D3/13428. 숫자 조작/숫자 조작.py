from itertools import combinations

def swap(string, a, b):
    string[a], string[b] = string[b], string[a]
    return string[a], string[b]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(map(str, input()))
    target = [i for i in range(len(data))] # target = [] \ for i in range(len(data)): target.append(i)
    min_val, max_val = int(''.join(data)), int(''.join(data))
    
    for val in combinations(target, 2):
        i, j = val
        swap(data, i, j)
        if data[0] == '0':
            swap(data, i, j)
            continue
        if int(''.join(data)) < min_val:
            min_val = int(''.join(data))
        if int(''.join(data)) > max_val:
            max_val = int(''.join(data))
        swap(data, i, j)
    print(f'#{test_case} {min_val} {max_val}')
  
        