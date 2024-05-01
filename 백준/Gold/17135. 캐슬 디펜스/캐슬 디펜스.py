import copy


# 조합 itertools 없이 하기
def comb(data, pick):
    for i in range(len(data)):
        if pick == 1:
            yield [data[i]]
        else:
            for j in comb(data[i+1:], pick-1):
                yield [data[i]] + j


# 공격
def attack(data):
    attack_list = []    # 가까운 적 리스트
    cnt = 0

    for da in data:
        pos = []        # 적 위치 확인 리스트
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 1:

                    distance = abs(i-n) + abs(j-da)
                    if d >= distance:   # 사정 거리
                        pos.append((distance, i, j))

        pos.sort(key=lambda x: (x[0], x[2])) # 1) 거리 가깝고 2) 왼쪽 기준 정렬
        if pos:
            attack_list.append(pos[0])

    # 제거
    for a in attack_list:
        _, i, j = a
        if temp[i][j] == 1:
            temp[i][j] = 0
            cnt += 1
    return cnt


# 적 아래로 이동
def move():
    for i in range(-1, -n, -1):
        temp[i] = temp[i-1]
    temp[0] = [0 for _ in range(m)]


# 적이 남아 있는지 확인 하기
def check():
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:
                return False
    return True


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
archer = [i for i in range(m)]
ans = 0

for value in comb(archer, 3):
    temp = copy.deepcopy(board)
    score = 0
    while not check():
        score += attack(value)
        move()
    ans = max(ans, score)

print(ans)