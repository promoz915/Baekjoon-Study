score = input()
score_alp = ['F', 'D', 'C', 'B', 'A']
result = float(score_alp.index(score[0]))

if result > 0:
    if score[1] == '+':
        result += 0.3
    elif score[1] == '-':
        result -= 0.3
print(result)