T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score_list = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        score = a * 0.35 + b * 0.45 + c * 0.2
        score_list.append(score)
    k_score = score_list[k-1]
    score_list.sort(reverse = True)
    idx = score_list.index(k_score) // (n//10)
    print(f'#{test_case} {grade[idx]}')