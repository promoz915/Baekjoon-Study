# DFM
import sys; input = sys.stdin.readline; sys.setrecursionlimit(10000)

n, m = map(int, input().split())        # n : 데이터 범위, m : 입력 줄 개수
arrive = False                          # 도착 확인 변수
a = [[] for _ in range(n+1)]            # 그래프 데이터 저장 인접 리스트
visited = [False] * (n+1)               # 방문 기록 저장 리스트

def DFS(now, depth):
    global arrive
    if depth == 5:                      # 깊이가 5라면 도착 완료 return
        arrive = True
        return
    visited[now] = True                 # 현재 노드 방문중 : True 입력
    for i in a[now]:                    # 현재 노드 데이터만큼 반복
        if not visited[i]:              # 방문하지 않은 노드가 있다면
            DFS(i, depth + 1)           # DFS 재귀함수, depth 1 증가
    visited[now] = False                # 방문 퇴장

for _ in range(m):                      # 양방항 에지이므로 양쪽에 에지 더하기
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n):                      # 노드 개수만큼 반복
    DFS(i, 1)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)