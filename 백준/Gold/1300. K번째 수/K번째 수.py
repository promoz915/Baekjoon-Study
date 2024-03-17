import sys; input = sys.stdin.readline

n = int(input())
k = int(input())

start, end, ans = 1, k, 0

# 이진 탐색 수행
while start <= end:
    middle = int((start + end) / 2)     # 중앙값
    cnt = 0
    
    # 중앙값보다 작은 수 계산
    for i in range(1, n+1):
        cnt += min(int(middle / i), n)  # cnt에 중앙 인덱스를 i로 나눈 값과 n 중 작은 값을 더함
    if cnt < k:                         # 현재 중앙값보다 작은 수의 개수가 k보다 작음
        start = middle + 1
    else:                               # 현재 중앙값보다 작은 수의 개수가 k보다 크거나 같음
        ans = middle                    # 정답 변수에 중앙값 저장
        end = middle - 1
print(ans)