T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr1 = list(map(list, zip(*arr[::-1])))
    arr2 = list(map(list, zip(*arr1[::-1])))
    arr3 = list(map(list, zip(*arr2[::-1])))
    
    print(f'#{test_case}')
    for i in range(n):
        print(''.join(map(str, arr1[i])), end=' ')
        print(''.join(map(str, arr2[i])), end=' ')
        print(''.join(map(str, arr3[i])))