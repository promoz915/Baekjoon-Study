n = int(input())
data = list(map(int, input().split()))
y, m = 0, 0
for d in data:
    y += (d//30 + 1) * 10
    m += (d//60 + 1) * 15

if y == m:
    print(f'Y M {y}')
elif y > m:
    print(f'M {m}')
else:
    print(f'Y {y}')