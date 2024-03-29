import sys; input = sys.stdin.readline

n, m = map(int, input().split())        # n : 수의 개수, m : 최솟값을 구하는 횟수
height = 0                              # 트리의 높이
length = n                              # 리프 노드 개수

# 트리 높이 구하기
while length != 0:
    length //= 2
    height += 1

tree_size = pow(2, height + 1)          # 트리 사이즈 구하기
left_index = tree_size // 2 - 1         # 리프 노드 시작 인덱스 구하기
tree = [sys.maxsize] * (tree_size + 1)  # 인덱스 트리 저장 리스트

for i in range(left_index + 1, left_index + n + 1):     # 리스트의 리프 노드 영역에 데이터 입력
    tree[i] = int(input())

# 인덱스 트리 생성 함수(최솟값 트리)
def make_tree(i):
    while i != 1:                       # 인덱스가 루트 노드(1)가 아닐 때까지
        if tree[i // 2] > tree[i]:      # 부모 노드와 비교하여 현재 노드 값이 더 작으면
            tree[i // 2] = tree[i]      # 값 업데이트
        i -= 1

# 초기 트리 생성
make_tree(tree_size - 1)                # 트리 사이즈-1 만큼 트리 생성

# 최솟값 계산 함수 생성
def get_min(s, e):
    num = sys.maxsize                   # 범위의 최솟값을 나타내는 변수, max_value로 초기화
    while s <= e:                       # 시작 인덱스와 종료 인덱스가 교차될 때까지
        if s % 2 == 1:
            num = min(num, tree[s])
            s += 1
        if e % 2 == 0:
            num = min(num, tree[e])
            e -= 1
        s //= 2
        e //= 2
    return num

for _ in range(m):
    s, e = map(int, input().split())
    s += left_index
    e += left_index
    print(get_min(s, e))