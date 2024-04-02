n = int(input())
word = ['3', '6', '9']

for i in range(1, n+1):
    cnt = 0
    for j in word:
        if j in str(i):
            cnt += str(i).count(j)
    if cnt == 0:
    	print(i, end=' ')
    else:
        print('-' * cnt, end=' ')