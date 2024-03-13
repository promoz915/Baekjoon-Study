num = int(input())
for _ in range(num):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')
    print()