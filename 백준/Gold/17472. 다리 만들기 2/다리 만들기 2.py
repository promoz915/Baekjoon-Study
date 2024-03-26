import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
myMap = [[0 for j in range(m)] for i in range(n)]           # 맵 정보 저장 리스트
visited = [[False for j in range(m)] for i in range(n)]     # BFS 시 방문 여부 저장 리스트

for i in range(n):
    myMap[i] = list(map(int, input().split()))

sNum = 1                        # 섬 번호
sumlist = list([])              # 모든 섬 정보 이중 리스트
mlist = []                      # 1개의 섬 정보 리스트

# 섬에 한 칸(노드)을 더해주는 함수
def addNode(i, j, queue):       
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)
    
# 탐색을 통해 섬 정보를 저장
def BFS(i, j):                 
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            
            # i, j 위치에서 네 방향으로 연결된 모든 노드를 탐색하여 1개 섬의 영역을 저장
            while r + tempR >= 0 and r + tempR < n and c + tempC >= 0 and c + tempC < m:
                
                # 연결된 새로운 노드가 확인되면 addNode를 통해 정보 저장
                if not visited[r + tempR][c + tempC] and myMap[r + tempR][c + tempC] != 0:
                    addNode(r + tempR, c + tempC, queue)
                else:
                    break
                if tempR < 0 :
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    return mlist

# 섬 구분 작업 수행
for i in range(n):
    for j in range(m):
        if myMap[i][j] != 0 and not visited[i][j]:
            
            # 깊은 복사로 해야 주소를 공유하지 않음
            tempList = copy.deepcopy(BFS(i, j))
            sNum += 1
            sumlist.append(tempList)

pq = PriorityQueue()

for now in sumlist:         # 모든 섬에서 지을 수 있는 다리를 찾고 저장
    for temp in now:        # 1개의 섬 정보
        r = temp[0]
        c = temp[1]
        now_S = myMap[r][c]
        for d in range(4):  # 4 방향 검색
            tempR = dr[d]
            tempC = dc[d]
            blength = 0
            while r + tempR >= 0 and r + tempR < n and c + tempC >= 0 and c + tempC < m:
                
                # 같은 섬이면 에지를 만들 수 없음
                if myMap[r + tempR][c + tempC] == now_S:
                    break
                
                # 같은 섬도 아니고 바다도 아니면
                elif myMap[r + tempR][c + tempC] != 0:
                    if blength > 1:     # 다른 섬 -> 길이가 1 이상일 때 에지로 더하기
                        pq.put((blength, now_S, myMap[r + tempR][c + tempC]))
                    break
                else:                   # 바다이면 다리의 길이 저장
                    blength += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 대표 노드 저장 리스트
parent = [0] * sNum         # 자기 자신을 대표 노드로 초기화

for i in range(len(parent)):
    parent[i] = i

useEdge = 0
result = 0

# 최소 신장 트리 알고리즘 수행
while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):  # 연결해도 사이클이 생기지 않으면
        union(s, e)
        result += v
        useEdge += 1

if useEdge == sNum - 2:     # sNum이 실제 섬의 수보다 1 크기 때문에 섬의 번호 표시를 위해 -2로 연산
    print(result)
else:
    print(-1)