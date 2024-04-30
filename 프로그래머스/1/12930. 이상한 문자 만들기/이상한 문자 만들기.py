def solution(s):
    answer = ''
    s_ = s.split(' ')
    for i in s_:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]