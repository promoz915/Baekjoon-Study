import sys; input = sys.stdin.readline

n, m, k = map(int, input().split())
height = 0
length = n

# 트리의 높이 구하기
while length != 0:
    length //= 2
    height += 1

tree_size = pow(2, height+1)            # 트리 사이즈 구하기
left_index = tree_size // 2 - 1         # 리프 노드 시작 인덱스
tree = [0] * (tree_size + 1)

for i in range(left_index + 1, left_index + n + 1):
    tree[i] = int(input())

# 인덱스로 트리 만들기
def make_tree(i):
    while i != 1:
        tree[i // 2] += tree[i]         # 부모 노드에 현재 인덱스의 트리값 더하기
        i -= 1

make_tree(tree_size - 1)

# 값 변경 함수
def change_val(idx, val):
    diff = val - tree[idx]
    while idx > 0:
        tree[idx] = tree[idx] + diff
        idx = idx // 2

# 구간 합 계산 함수
def get_sum(s, e):
    sum_val = 0
    while s <= e:
        if s % 2 == 1:
            sum_val += tree[s]
            s += 1
        if e % 2 == 0:
            sum_val += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return sum_val

for _ in range(m+k):
    val, s, e = map(int, input().split())
    if val == 1:
        change_val(left_index + s, e)
    elif val == 2:
        s += left_index
        e += left_index
        print(get_sum(s, e))