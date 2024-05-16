import sys
input = sys.stdin.readline

data = input().rstrip()
cnt = 0

max_val, min_val = "", ""

for i in data:
    if i == 'M':
        cnt += 1
    else:
        if cnt > 0:
            max_val += str(5 * (10 ** cnt))
            min_val += str(10 ** cnt + 5)
        else:
            max_val += '5'
            min_val += '5'
        cnt = 0

if cnt > 0:
    max_val += '1' * cnt
    min_val += str(10 ** (cnt - 1))

print(max_val)
print(min_val)