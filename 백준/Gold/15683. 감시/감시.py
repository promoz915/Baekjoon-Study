import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cam_data = {1: [[0], [1], [2], [3]],
            2: [[1, 3], [0, 2]],
            3: [[0, 1], [1, 2], [2, 3], [3, 0]],
            4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
            5: [[0, 1, 2, 3]]}
min_val = 1e9
cam = []
# 카메라가 있으면 cam 리스트에 추가
for i in range(n):
    for j in range(m):
        if 0 < data[i][j] < 6:
            cam.append((i, j, data[i][j]))

# 현재 depth와 맵 정보 h를 받음
def to_hash(h, arr, x, y):
    for a in arr:
        nx, ny = x, y
        while True:
            nx += dv[a][0]
            ny += dv[a][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or h[nx][ny] == 6:
                break
            elif h[nx][ny] == 0:
                h[nx][ny] = -1

def dfs(depth, h):
    global min_val
    # depth와 cam 수가 같으면
    if depth == len(cam):
        cnt = 0
        # 현재 맵에 있는 사각지대의 수를 세고
        for hh in h:
            cnt += hh.count(0)
        # 사각지대 최솟값보다 구한 cnt가 더 작으면 업데이트
        min_val = min(min_val, cnt)
        return
    # 같지 않으면
    # 깊은 복사
    maps = copy.deepcopy(h)
    x, y, n = cam[depth]
    
    for cd in cam_data[n]:
        to_hash(maps, cd, x, y)
        dfs(depth+1, maps)
        maps = copy.deepcopy(h)

dfs(0, data)
print(min_val)