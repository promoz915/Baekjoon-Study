start = int(input())
end = int(input())
arr = []

for i in range(start, end+1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)