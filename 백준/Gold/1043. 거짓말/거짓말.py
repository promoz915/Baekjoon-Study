import sys; input = sys.stdin.readline

n, m = map(int, input().split())
trueP = list(map(int, input().split()))             # 진실을 아는 사람 저장
T = trueP[0]                                        # 진실을 아는 사람 수
del trueP[0]
result = 0
party = [[] for _ in range(m)]

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

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(m):
    party[i] = list(map(int, input().split()))      # 파티 데이터 저장
    del party[i][0]

parent = [0] * (n+1)

for i in range(n+1):                                # 대표 노드를 자기 자신으로 초기화
    parent[i] = i

for i in range(m):                                  # 각 파티에 참여한 사람들을 1개의 그룹으로 만들기
    firstPeople = party[i][0]
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

# 각 파티의 대표 노드와 진실을 아는 사람들의 대표 노드가 같다면 과장할 수 없음
for i in range(m):
    isPossible = True
    firstPeople = party[i][0]
    for j in range(len(trueP)):
        if find(firstPeople) == find(trueP[j]):
            isPossible = False
            break
    if isPossible:
        result += 1                                 # 모두 다르면 결괏값 1 증가

print(result)