import sys; input = sys.stdin.readline

n = int(input())
d = [0] * (n+2)             # i ~ 퇴사일까지 벌 수 있는 최대 수입 저장
t = [0] * (n+1)             # 상담에 필요한 일 수 저장
p = [0] * (n+1)             # 상담을 완료했을 때 받는 수입 저장

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i + t[i] > n + 1:    # i번째 상담을 퇴사일까지 끝낼 수 없을 때
        d[i] = d[i+1]
    else:
        # i+1일 ~ 퇴사일에 벌 수 있는 최대 수입, i번째 상담 비용 + i번째 상담이 끝난 다음 날부터 퇴사일까지의 수입
        d[i] = max(d[i+1], p[i] + d[i+t[i]])

print(d[1])                 # 1일부터 퇴사일까지 벌 수 있는 최대 수입