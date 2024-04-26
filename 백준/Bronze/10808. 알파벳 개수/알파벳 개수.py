n = input()
check = [0] * 26
for i in n:
    check[ord(i) - 97] += 1

for i in check:
    print(i, end=' ')