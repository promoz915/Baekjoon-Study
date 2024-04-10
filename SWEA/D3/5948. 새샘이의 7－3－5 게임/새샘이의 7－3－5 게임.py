from itertools import combinations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    ans = []
    for i in combinations(data, 3):
        ans.append(sum(i))
    ans = list(set(ans))
    ans.sort(reverse=True)
    print(f'#{test_case} {ans[4]}')