T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = input().split()
    word = list(input().split())
    keys = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dict = {key: 0 for key in keys}
	    
    for i in word:
        dict[i] += 1
    print(n)
    for i, j in dict.items():
        print(f'{i} ' * j, end = ' ')
    print()