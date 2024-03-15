import sys; input = sys.stdin.readline

n, q = map(int, input().split())
cnt_list = list(map(int, input().split()))

cnt = 0
arr = [0]

for i in cnt_list:
    cnt += i
    arr.append(cnt)

idx = 0

for i in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 3:
        a, b = cmd[1], cmd[2]
        a = (a - 1 + idx) % n
        b = (b - 1 + idx) % n
        if a <= b:
            print(arr[b+1] - arr[a])
        else:
            print(arr[n] - arr[0] - (arr[a] - arr[b + 1]))
    else:
        idx += -(cmd[1]) if cmd[0] == 1 else cmd[1]
        idx = (idx + n) % n