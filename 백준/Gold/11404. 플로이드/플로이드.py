import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0                  # 인접 행렬에 시작 도시와 종료 도시가 같은 자리에 0 저장

for i in range(m):
    s, e, w = map(int, input().split())
    if distance[s][e] > w:
        distance[s][e] = w

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == sys.maxsize:   # 리스트의 값이 최초 초기화하기에 충분한 큰 수 일 경우 0 출력
            print(0, end=' ')               # 도착할 수 없는 경로일 때
        else:
            print(distance[i][j], end=' ')
    print()