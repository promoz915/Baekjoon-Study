def solution(dartResult):
    temp = ''
    score = []
    for i in dartResult:
        if i.isdigit():
            temp += i
        elif i == 'S':
            score.append(int(temp)**1)
            temp = ''
        elif i == 'D':
            score.append(int(temp)**2)
            temp = ''
        elif i == 'T':
            score.append(int(temp)**3)
            temp = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        else:
            score[-1] *= -1
    return sum(score)