a = int(input())
for _ in range(a):
    ox_list = list(input())
    num = 0
    sum = 0
    for ox in ox_list:
        if ox == 'O':
            num += 1
            sum += num
        else:
            num = 0
    print(sum)