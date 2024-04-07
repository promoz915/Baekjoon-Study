import math

MOD = 10**6
a = [0] * (MOD+1)

for i in range(2, MOD+1):
    a[i] = i

for i in range(2, int(math.sqrt(MOD)) + 1):
    if a[i] == 0:
         continue
    for j in range(i+i, MOD+1, i):
        a[j] = 0
for i in range(MOD+1):
    if a[i] != 0:
        print(a[i], end=' ')