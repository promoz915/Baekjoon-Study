import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()
sum = 0

for i in range(n):
    tempc = list(input())
    for j in range(n):
        temp = 0
        if 'a' <= tempc[j] <= 'z':                  # 소문자일 때
            temp = ord(tempc[j]) - ord('a') + 1
        elif 'A' <= tempc[j] <= 'Z':                # 대문자일 때
            temp = ord(tempc[j]) - ord('A') + 27
        sum += temp                                 # 총 랜선의 길이 저장
        if i != j and temp != 0:
            pq.put((temp, i, j))                    # 정렬 순서를 고려하여 input 데이터 순서 설정

parent = [0] * n

for i in range(n):
    parent[i] = i

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

useEdge = 0
result = 0

# 최소 신장 트리 알고리즘 수행
while pq.qsize() > 0:
    v, s, e = pq.get()

    # 에지 시작점과 끝점의 부모 노드가 다르면
    if find(s) != find(e):      # 연결해도 사이클이 생기지 않으면
        union(s, e)
        result += v
        useEdge += 1

if useEdge == n-1:
    print(sum - result)         # 모든 랜선의 합에서 최소 신장 트리의 결괏값을 뺀 값을 출력
else:
    print(-1)