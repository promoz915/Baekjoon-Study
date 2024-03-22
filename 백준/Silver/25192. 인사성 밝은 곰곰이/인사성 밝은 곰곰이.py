def gom(n):
    gom = set()
    cnt = 0
    for _ in range(n):
        word = input()
        if word != 'ENTER':
            if word not in gom:
                cnt += 1
                gom.add(word)
        elif word == 'ENTER':
            gom.clear()
    return cnt
print(gom(int(input())))