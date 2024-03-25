import sys; input = sys.stdin.readline

n = int(input())
distance = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    distance[i] = list(map(int, input().split()))


for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][k] == 1 and distance[k][j] == 1: # k를 거치는 모든 경로중 1개라도 연결된 경로가 있다면
                distance[i][j] = 1                          # i와 j는 연결노드로 취급

for i in range(n):
    for j in range(n):
        print(distance[i][j], end=' ')
    print()