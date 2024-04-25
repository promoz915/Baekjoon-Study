data = [int(input()) for _ in range(5)]
for i in range(5):
    if data[i] < 40:
        data[i] = 40
score = sum(data) // 5
print(score)