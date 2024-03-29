import sys; input = sys.stdin.readline

n, m, k = map(int, input().split())     # n : 수의 개수, m : 변경이 일어나는 개수, k : 구간 곱을 구하는 개수
height = 0                              # 트리의 높이
length = n                              # 리프 노드 개수
MOD = 1000000007

# 트리 높이 구하기
while length != 0:
    length //= 2
    height += 1

tree_size = pow(2, height + 1)          # 트리 사이즈 구하기
left_index = tree_size // 2 - 1         # 리프 노드 시작 인덱스
tree = [1] * (tree_size + 1)            # 곱하기이므로 초깃값은 1로 설정

# 데이터를 리프 노드에 저장
for i in range(left_index + 1, left_index + n + 1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def make_tree(i):
    while i != 1:
        tree[i // 2] = tree[i // 2] * tree[i] % MOD
        i -= 1

make_tree(tree_size - 1)                # 초기 트리 생성

# 값 변경 함수
def change_val(idx, val):
    tree[idx] = val
    while idx > 1:
        idx = idx // 2
        
        # 부모 노드에 두 자식 노드값을 곱하고 나머지 연산 후 저장
        tree[idx] = tree[idx * 2] % MOD * tree[idx * 2 + 1] % MOD

# 구간 곱 계산 함수
def get_mul(s, e):
    num = 1
    while s <= e:
        if s % 2 == 1:
            num = num * tree[s] % MOD
            s += 1
        if e % 2 == 0:
            num = num * tree[e] % MOD
            e -= 1
        s = s // 2
        e = e // 2
    return num

for _ in range(m + k):
    val, s, e = map(int, input().split())
    if val == 1:
        change_val(left_index + s, e)
    elif val == 2:
        s = s + left_index
        e = e + left_index
        print(get_mul(s, e))