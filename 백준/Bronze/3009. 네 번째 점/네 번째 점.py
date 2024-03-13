xarr = []
yarr = []
for _ in range(3):
    x, y = map(int, input().split())
    xarr.append(x)
    yarr.append(y)

for i in range(3):
    if xarr.count(xarr[i]) == 1:
        x4 = xarr[i]
    if yarr.count(yarr[i]) == 1:
        y4 = yarr[i]

print(x4, y4)