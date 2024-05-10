from itertools import combinations

l, c = map(int, input().split())
word = input().split()
combs = combinations(sorted(word), l)
ans = []

for comb in combs:
    cnt = 0
    temp = 0
    for c in comb:
        if c in "aeiou":
            cnt += 1
        else:
            temp += 1
    if cnt >= 1 and temp >= 2:
        print(''.join(comb))