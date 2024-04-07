def check(num):
    for i in range(num):
        if row[i] == row[num] or abs(row[num] - row[i]) == abs(num - i):
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
                
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    row = [0] * n
    ans = 0
    queen(0)
    print(f'#{test_case} {ans}')