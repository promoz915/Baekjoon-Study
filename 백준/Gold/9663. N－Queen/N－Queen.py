import sys; input = sys.stdin.readline
n = int(input())

ans = 0
row = [0] * n

def check(num):
    for i in range(num):
        if row[num] == row[i] or abs(row[num] - row[i]) == abs(num - i):
            return False

    return True


def queen(num):
    global ans
    if num == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[num] = i
            if check(num):
                queen(num+1)

queen(0)
print(ans)