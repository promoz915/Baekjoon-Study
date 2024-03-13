import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
g = []
for _ in range(n):
    g.extend(map(int, input().split()))     # n개의 줄의 원소들을 한 줄로 정리

time = [0 for i in range(257)]              # time[k]에 땅높이 k일때 소요시간 저장
h = 0
for i in range(257):                        # i는 현재 땅높이가 된다
    block = b                               # 가지고 있는 블록 갯수
    for j in g:
        if j <= i:                          # 쌓기
            time[i] += i - j                # i(목표 높이) - j(쌓을 높이) 만큼 소요 time 저장
            block -= i - j                  # 쌓는 블록 갯수
        else:                               # 부수기
            time[i] += 2 * (j - i)          # j(부술 높이) - i(목표 높이) 만큼 소요 time 저장
            block += j - i                  # 부숴서 남는 블록 갯수
    if block >= 0 and time[i] <= time[h]:   # 블록이 있는지 체크 | 답이 여러개 있으면 땅의 높이가 가장 높은 것 저장
        h = i                               # 최소 소요 time 저장
print(time[h], h)