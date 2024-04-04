import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for i in range(n)]

# 현재도시 c, 방문한 도시 리스트 v일 때 남은 모든 도시를 경유하는 데 필요한 최소 비용 테이블
d = [[0 for j in range(1 << 16)] for i in range(16)]

def func(c, v):
    if v == (1 << n) - 1:       # 모든 도시를 방문한 경우
        if w[c][0] == 0:        # 출발점으로 돌아갈 수 없는 경우
            return float('inf')
        else:
            return w[c][0]

    if d[c][v] != 0:            # 메모이제이션
        return d[c][v]

    min_val = float('inf')      # 초기 최솟값 설정

    for i in range(n):          # 모든 도시에 대해
        if (v&(1<<i)) == 0 and w[c][i] != 0:        # 방문한 적이 없고, 갈 수 있는 도시인 경우
            min_val = min(min_val, func(i, (v | (1 << i))) + w[c][i])   # 최소 비용 갱신
    d[c][v] = min_val           # 계산된 최소 비용 저장
    return d[c][v]

print(func(0, 1))