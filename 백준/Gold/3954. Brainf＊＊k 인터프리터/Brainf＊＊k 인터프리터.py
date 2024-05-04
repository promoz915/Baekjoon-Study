import sys
input = sys.stdin.readline

def func(mark):
    global sm, sc, si, p, code_idx, data_idx, max_code_idx

    if mark == '-':
        arr[p] -= 1
        arr[p] %= 256
    elif mark == '+':
        arr[p] += 1
        arr[p] %= 256
    elif mark == "<":
        p -= 1
        p %= sm
    elif mark == ">":
        p += 1
        p %= sm
    elif mark == '[':
        if arr[p] == 0:
            code_idx = teleport[code_idx]
    elif mark == ']':
        if arr[p] != 0:
            code_idx = teleport[code_idx]
    elif mark == '.':
        pass
    elif mark == ',':
        if data_idx < si:
            arr[p] = ord(data[data_idx])
            data_idx += 1
        else:
            arr[p] = 255


def check():
    global sc, code_idx, max_code_idx

    cnt = 0
    while code_idx < sc:
        cnt += 1
        func(code[code_idx])
        if cnt >= 50000000:
            max_code_idx = min(max_code_idx, code_idx)
        code_idx += 1
        if cnt >= 2 * 50000000:
            print(f'Loops {max_code_idx} {teleport[max_code_idx]}')
            return
    print('Terminates')
    return


def is_loop(code):
    teleport = {}
    save = []
    for idx, c in enumerate(code):
        if c == '[':
            save.append(idx)
        elif c == ']':
            to = save.pop()
            teleport[idx] = to
            teleport[to] = idx
    return teleport


t = int(input())
for test_case in range(1, t+1):
    sm, sc, si = map(int, input().split())
    code = input()
    data = input()

    arr = [0] * sm
    p = 0
    code_idx = 0
    data_idx = 0
    max_code_idx = sc
    teleport = is_loop(code)

    check()