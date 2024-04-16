dict = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    cnt = 0
    word = input()
    if word == '#':
        break
    for target in word:
        if target in dict:
            cnt += 1
    print(cnt)